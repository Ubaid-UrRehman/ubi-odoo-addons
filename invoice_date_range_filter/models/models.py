# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta, date, datetime

class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    subscription = fields.Boolean(default=True)
    date_from = fields.Date('From')
    date_to = fields.Date("To")
    paying_date = fields.Date("Paying Date")

    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        result = []
        filter_date = ''
        no_days_values = self.env['ir.values'].search_read([('name','=','no_days')], fields=['value_unpickle'])
        if 'filter_subscription_expiry' in self._context:
            for no_days_val in no_days_values:
                filter_date = (date.today() + timedelta(days=int(no_days_val['value_unpickle']))).strftime("%Y-%m-%d")

            if filter_date:
                account_invoice_search = """select id from account_invoice where date_to <= '{}' and state in {};""".format(filter_date,('paid','open'))
                self._cr.execute(account_invoice_search)
                invoices = self._cr.fetchall()
                for ids in invoices:
                    result.append(ids[0])
            if not args:
                args = [['id','in',result]]
            else:
                args.append(['id','in',result])
        if 'filter_pay_before_subscription_expiry' in self._context:
            query_serach = "select id from account_invoice where paying_date < date_from;"
            self._cr.execute(query_serach)
            invoices = self._cr.fetchall()
            for ids in invoices:
                result.append(ids[0])
            if not args:
                args = [['id','in',result]]
            else:
                args.append(['id','in',result])
                args.append(['id','in',result])
        if 'filter_pay_after_subscription_expiry' in self._context:
            query_serach = "select id from account_invoice where paying_date >= date_from and paying_date <= date_to;"
            self._cr.execute(query_serach)
            invoices = self._cr.fetchall()
            for ids in invoices:
                result.append(ids[0])
            if not args:
                args = [['id','in',result]]
            else:
                args.append(['id','in',result])


        return super(AccountInvoice, self).search(args, offset, limit, order, count)

    @api.onchange('subscription')
    def set_dates_fields_empty(self):
        if not self.subscription:
            self.date_from = ''
            self.date_to = ''

class AccountPayment(models.Model):
    _inherit = "account.payment"


    @api.model
    def create(self, values):
        if values.get('communication', None):
            invoice = self.env["account.invoice"].search([('number','=', values.get('communication'))])
            invoice.write({'paying_date':values.get('payment_date')})
        return super(AccountPayment, self).create(values)