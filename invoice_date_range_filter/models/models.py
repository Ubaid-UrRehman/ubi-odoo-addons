# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

# datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    subscription = fields.Boolean()
    date_from = fields.Date('From')
    date_to = fields.Date("To")

    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        result = []
        start_date = ''
        satrt_date_values = self.env['ir.values'].search_read([('name','=','date_start')], fields=['value_unpickle'])
        end_date_value = self.env['ir.values'].search_read([('name','=','date_end')], fields=['value_unpickle'])
        if 'filter_subscription_expiry' in self._context:
            for start_date_val in satrt_date_values:
                if start_date_val['value_unpickle'] != 'False':
                    start_date = datetime.strptime(start_date_val['value_unpickle'], '%Y-%m-%d').strftime('%Y-%m-%d')
            for end_date_val in end_date_value:
                if end_date_val['value_unpickle'] != 'False':
                    end_date = datetime.strptime(end_date_val['value_unpickle'], '%Y-%m-%d').strftime('%Y-%m-%d')
            if start_date and end_date:
                account_invoice_search = """select id from account_invoice where date_from >= '{}' and date_to <= '{}' and state in {};""".format(start_date,end_date,('paid','open'))
                self._cr.execute(account_invoice_search)
                invoices = self._cr.fetchall()
                for ids in invoices:
                    result.append(ids[0])
            if not args:
                args = [['id','in',result]]
            else:
                args.append(['id','in',result])

        return super(AccountInvoice, self).search(args, offset, limit, order, count)
    
