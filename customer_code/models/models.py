# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    unique_id = fields.Integer(string='Customer code', required=False, help="The Unique Sequence no")

    @api.constrains('unique_id')
    def _check_unique_id(self):
        for record in self:
            if record.unique_id:
                print record.unique_id
                print str(record.unique_id)
                print len(str(record.unique_id))
                if len(str(record.unique_id)) > 10 or len(str(record.unique_id)) < 10:
                    raise ValidationError("Code must be 10 digits long")

    _sql_constraints = [
        ('unique_id_unique',
         'UNIQUE(unique_id)',
         "The code must be unique"),
    ]