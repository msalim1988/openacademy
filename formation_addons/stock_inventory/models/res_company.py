# -*- coding: utf-8 -*-

from odoo import api, fields, models

class ResCompany(models.Model):
    _inherit = 'res.company'

    inventory_inprogress = fields.Boolean('Inventaire en cours', readonly=True)
    read_only_models = fields.Many2many(comodel_name="ir.model", string="Objet en lecture seule")
