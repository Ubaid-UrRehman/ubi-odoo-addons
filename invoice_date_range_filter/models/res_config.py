# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class SaleConfigSettings(models.TransientModel):
    _inherit = 'sale.config.settings'

    no_days = fields.Integer(string='Number of Days', required=False)

    @api.multi
    def set_no_days_defaults(self):
        return self.env['ir.values'].sudo().set_default(
            'sale.config.settings', 'no_days', self.no_days)