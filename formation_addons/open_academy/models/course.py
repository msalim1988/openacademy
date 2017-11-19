# -*- coding: utf-8 -*-
from odoo import api, fields, models


class OpenAcademyCourse(models.Model):

    _name = 'openacademy.course'
    _rec_name = 'titre'

    titre = fields.Char(string='Titre du cours', required=True)
    description = fields.Text()