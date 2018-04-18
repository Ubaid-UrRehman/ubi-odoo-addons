# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools
from odoo.exceptions import ValidationError

class CrmLead(models.Model):
    _inherit = "crm.lead"

    customer_code = fields.Char('Code', required=True)

    def _onchange_partner_id_values(self, partner_id):
        """ returns the new values when partner_id has changed """
        if partner_id:
            partner = self.env['res.partner'].browse(partner_id)

            partner_name = partner.parent_id.name
            if not partner_name and partner.is_company:
                partner_name = partner.name

            return {
                'partner_name': partner_name,
                'contact_name': partner.name if not partner.is_company else False,
                'title': partner.title.id,
                'street': partner.street,
                'street2': partner.street2,
                'city': partner.city,
                'state_id': partner.state_id.id,
                'country_id': partner.country_id.id,
                'email_from': partner.email,
                'phone': partner.phone,
                'mobile': partner.mobile,
                'fax': partner.fax,
                'zip': partner.zip,
                'function': partner.function,
                'customer_code': partner.unique_id
            }
        return {}

    @api.multi
    def _create_lead_partner(self):
        """ Create a partner from lead data
            :returns res.partner record
        """
        contact_name = self.contact_name
        res_partner = self.env["res.partner"]
        customer_obj = res_partner.search([('unique_id', '=', self.customer_code)])
        if customer_obj:
            raise ValidationError("You are allow to create new customer. Customer {} already exist".format(customer_obj.name))
        if not contact_name:
            contact_name = self.env['res.partner']._parse_partner_name(self.email_from)[0] if self.email_from else False

        if self.partner_name:
            partner_company = self._lead_create_contact(self.partner_name, True)
        elif self.partner_id:
            partner_company = self.partner_id
        else:
            partner_company = None

        if contact_name:
            return self._lead_create_contact(contact_name, False, partner_company.id if partner_company else False)

        if partner_company:
            return partner_company
        return self._lead_create_contact(self.name, False)

    @api.multi
    def _lead_create_contact(self, name, is_company, parent_id=False):
        """ extract data from lead to create a partner
            :param name : furtur name of the partner
            :param is_company : True if the partner is a company
            :param parent_id : id of the parent partner (False if no parent)
            :returns res.partner record
        """
        email_split = tools.email_split(self.email_from)
        values = {
            'name': name,
            'user_id': self.env.context.get('default_user_id') or self.user_id.id,
            'comment': self.description,
            'team_id': self.team_id.id,
            'parent_id': parent_id,
            'phone': self.phone,
            'mobile': self.mobile,
            'email': email_split[0] if email_split else False,
            'fax': self.fax,
            'title': self.title.id,
            'function': self.function,
            'street': self.street,
            'street2': self.street2,
            'zip': self.zip,
            'city': self.city,
            'country_id': self.country_id.id,
            'state_id': self.state_id.id,
            'is_company': is_company,
            'type': 'contact',
            # 'unique_id':self.customer_code
        }
        if self.contact_name and self.partner_name:
            if is_company:
                values.update({'unique_id':self.customer_code})
        elif self.contact_name and not self.partner_name:
            values.update({'unique_id':self.customer_code})
        elif not self.contact_name and self.partner_name:
            values.update({'unique_id':self.customer_code})
        else:
            values.update({'unique_id':self.customer_code})
        return self.env['res.partner'].create(values)