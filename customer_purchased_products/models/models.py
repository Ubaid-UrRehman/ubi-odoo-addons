# -*- coding: utf-8 -*-

from odoo import models, fields, api,_

class ResPartner(models.Model):
    _inherit = 'res.partner'

    total_product_count = fields.Integer(compute='_total_product_count', string="Total Products")

    @api.multi
    def open_partner_product_buying_history(self):
        print self
        # ctx = self.env._context()
        product_template_ids_list = []
        product_ids_lsit = self.get_all_products_ids_form_customer_invoice_line()
        product_obj = self.env['product.product'].search([('id', 'in', product_ids_lsit)])
        for item in product_obj:
            product_template_ids_list.append(item.product_tmpl_id.id)
        print 'product_ids_lsit',product_ids_lsit,'product_template_ids_list',product_template_ids_list
        ir_model_data = self.env['ir.model.data']
        try:
           tree_id = ir_model_data.get_object_reference('customer_purchased_products', 'product_tempalte_view_for_customer')[1]
           form_id = ir_model_data.get_object_reference('product', 'product_template_only_form_view')[1]
           print 'tree_id',tree_id
           print 'form_id',form_id
        except ValueError:
            view_id = False

        # partner_id = self.ren9.id
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
        print "self",self
        # product_ids_lsit = []
        if not self.ids:
            self.total_product_count = 0.0
            return True
        # all_partners_and_children = {}
        # all_partner_ids = []
        product_ids_lsit = self.get_all_products_ids_form_customer_invoice_line()
        print len(set(product_ids_lsit))
        for partner in self:
            partner.total_product_count = len(set(product_ids_lsit))

    def get_all_products_ids_form_customer_invoice_line(self):
        product_ids_lsit = []
        all_partners_and_children = {}
        all_partner_ids = []
        for partner in self:
            print
            partner
            # price_total is in the company currency
            all_partners_and_children[partner] = self.with_context(active_test=False).search(
                [('id', 'child_of', partner.id)]).ids
            all_partner_ids += all_partners_and_children[partner]
        print set(all_partner_ids)
        all_invoices = self.env['account.invoice'].search([('partner_id', 'in', all_partner_ids),
                                                           ('type', 'in', ('out_invoice', 'out_refund'))])
        print all_invoices
        for item in all_invoices:
            for line in item.invoice_line_ids:
                print
                line.product_id
                product_ids_lsit.append(line.product_id.id)
        return product_ids_lsit

class ProductTemplate(models.Model):
    _inherit = "product.template"

    @api.multi
    def view_invoices_of_product(self):
        print self, self.id, self._context
        partner_id = self._context.get('active_id', None)
        product_ids_lsit = [product.id for product in self.env['product.product'].search([('product_tmpl_id', '=', self.id)])]
        print "partner_id",partner_id, 'product_ids_lsit',product_ids_lsit
        invoice_line_obj = self.env['account.invoice.line'].search([('partner_id', '=', partner_id),('product_id', 'in', product_ids_lsit)])
        print 'invoice_line_obj',invoice_line_obj
        invoice_id_list = [invoice.invoice_id.id for invoice in invoice_line_obj]
        print 'invoice_id_list',invoice_id_list
        ir_model_data = self.env['ir.model.data']
        try:
           tree_id = ir_model_data.get_object_reference('account', 'invoice_tree')[1]
           form_id = ir_model_data.get_object_reference('account', 'invoice_form')[1]
           print 'tree_id',tree_id
           print 'form_id',form_id
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