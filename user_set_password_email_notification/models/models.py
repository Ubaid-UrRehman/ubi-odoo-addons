# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResUsers(models.Model):
    _inherit = 'res.users'

    @api.model
    def create(self, values):
    	res = super(ResUsers, self.with_context({'no_reset_password': False})).create(values)
    	return res