# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    analytic_account_id = fields.Many2one(
        comodel_name='account.analytic.account',
        string='Analytic Account',
    )

    @api.multi
    def _prepare_invoice_line(self, qty):
        print "inherited"
        self.ensure_one()
        res = super(SaleOrderLine, self)._prepare_invoice_line(qty)
        print res
        if self.analytic_account_id:
            res.update({
                'account_analytic_id': self.analytic_account_id.id,
                })
        print "update, res",res
        return res
