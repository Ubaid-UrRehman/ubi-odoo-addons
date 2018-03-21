# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    unique_id = fields.Char(string='Customer code', required=False, help="The Unique Sequence no")

    @api.constrains('unique_id')
    def _check_unique_id(self):
        for record in self:
            if record.unique_id:
                if len(record.unique_id) > 25:
                    raise ValidationError("More than 25 characters are not allowed")

    _sql_constraints = [
        ('unique_id_unique',
         'UNIQUE(unique_id)',
         "The code must be unique"),
    ]