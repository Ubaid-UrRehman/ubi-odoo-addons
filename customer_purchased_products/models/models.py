# -*- coding: utf-8 -*-

from odoo import models, fields, api,_

class ResPartner(models.Model):
    _inherit = 'res.partner'

    total_product_count = fields.Integer(compute='_total_product_count', string="Total Products")

    @api.multi
    def open_partner_product_buying_history(self):
        product_template_ids_list = []
        product_ids_lsit = self.get_all_products_ids_form_customer_invoice_line()
        product_obj = self.env['product.product'].search([('id', 'in', product_ids_lsit)])
        for item in product_obj:
            product_template_ids_list.append(item.product_tmpl_id.id)
        ir_model_data = self.env['ir.model.data']
        try:
           tree_id = ir_model_data.get_object_reference('customer_purchased_products', 'product_tempalte_view_for_customer')[1]
           form_id = ir_model_data.get_object_reference('product', 'product_template_only_form_view')[1]
        except ValueError:
            view_id = False

        return {
            'name': _('Products'),
            'type': 'ir.actions.act_window',
            'domain': [('id', 'in', product_template_ids_list)],
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'product.template',
            'view_id': False,
            'views': [(tree_id, 'tree'),(form_id, 'form')],
            'target': 'current',
            'context': self.env.context,
        }

    @api.multi
    def _total_product_count(self):
        if not self.ids:
            self.total_product_count = 0.0
            return True

        product_ids_lsit = self.get_all_products_ids_form_customer_invoice_line()
        for partner in self:
            partner.total_product_count = len(set(product_ids_lsit))

    def get_all_products_ids_form_customer_invoice_line(self):
        product_ids_lsit = []
        all_partners_and_children = {}
        all_partner_ids = []
        for partner in self:
            # price_total is in the company currency
            all_partners_and_children[partner] = self.with_context(active_test=False).search(
                [('id', 'child_of', partner.id)]).ids
            all_partner_ids += all_partners_and_children[partner]
        all_invoices = self.env['account.invoice'].search([('partner_id', 'in', all_partner_ids),
                                                           ('type', 'in', ('out_invoice', 'out_refund'))])
        for item in all_invoices:
            for line in item.invoice_line_ids:
                product_ids_lsit.append(line.product_id.id)
        return product_ids_lsit

class ProductTemplate(models.Model):
    _inherit = "product.template"

    @api.multi
    def view_invoices_of_product(self):
        partner_id = self._context.get('active_id', None)
        product_ids_lsit = [product.id for product in self.env['product.product'].search([('product_tmpl_id', '=', self.id)])]
        invoice_line_obj = self.env['account.invoice.line'].search([('partner_id', '=', partner_id),('product_id', 'in', product_ids_lsit)])
        invoice_id_list = [invoice.invoice_id.id for invoice in invoice_line_obj]
        ir_model_data = self.env['ir.model.data']
        try:
           tree_id = ir_model_data.get_object_reference('account', 'invoice_tree')[1]
           form_id = ir_model_data.get_object_reference('account', 'invoice_form')[1]
        except ValueError:
            view_id = False
        return {
            'name': _('Customer Invoices'),
            'type': 'ir.actions.act_window',
            'domain': [('id', 'in', invoice_id_list)],
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'account.invoice',
            'view_id': False,
            'views': [(tree_id, 'tree'),(form_id, 'form')],
            'target': 'current',
            'context': self.env.context,
        }
        # account.invoice_tree, account.invoice_form