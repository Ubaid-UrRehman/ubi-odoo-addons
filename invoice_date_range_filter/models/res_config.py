# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class SaleConfigSettings(models.TransientModel):
    _inherit = 'sale.config.settings'

    date_start = fields.Date(string='Start date', required=False)
    date_end = fields.Date(string='End date', required=False)

    @api.multi
    def set_date_start_defaults(self):
        return self.env['ir.values'].sudo().set_default(
            'sale.config.settings', 'date_start', self.date_start)

    @api.multi
    def set_date_end_defaults(self):
        return self.env['ir.values'].sudo().set_default(
            'sale.config.settings', 'date_end', self.date_end)
