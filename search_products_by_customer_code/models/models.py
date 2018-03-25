# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductTempalte(models.Model):
    _inherit = "product.template"

    product_customer_code_ids = fields.One2many(
        'product.customer.code', 'product_id', string='Product customer codes',
        copy=False, help="Different codes that has the product for each "
        "partner.")

class ProductCustomerCode(models.Model):

    _name = "product.customer.code"
    _description = "Add many Customer's Code"

    _rec_name = 'product_code'

    product_code = fields.Char('Customer Code', required=False,
                               help="This customer's product "
                               "code will be used when searching into a "
                               "request for quotation.")
    product_id = fields.Many2one('product.template', 'Product', required=True,
                                 help='Product Identification')
    partner_id = fields.Many2one('res.partner', 'Customer', required=True,
                                 help='Partner Reference')
class AccountInvoiceLine(models.Model):
    _inherit = "account.invoice.line"

    @api.model
    def create(self, values):
        product_customer_code_values = {}
        res = super(AccountInvoiceLine, self).create(values)
        if res.invoice_id.type == 'out_invoice':
            product_customer_code_values['product_code'] = res.partner_id.unique_id
            product_customer_code_values['product_id'] = res.product_id.product_tmpl_id.id
            product_customer_code_values['partner_id'] = res.partner_id.id
            self.env['product.customer.code'].create(product_customer_code_values)
        return res