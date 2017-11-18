# -*- coding: utf-8 -*-
from odoo import api, _
from odoo.exceptions import AccessError
from odoo.models import BaseModel

native_create = BaseModel.create
native_write = BaseModel.write
native_unlink = BaseModel.unlink


@api.model
@api.returns('self', lambda value: value.id)
def create(self, vals):
    if self._name in ['sale.order'] and self.env.user.company_id.inventory_inprogress:
        raise AccessError(_('Un inventaire est en cours contacter votre administrateur.'))
    return native_create(self, vals)


@api.multi
def write(self, vals):
    company = self.env.user.company_id
    if self._name in company.read_only_models.mapped('model') and company.inventory_inprogress:
        raise AccessError(_('Un inventaire est en cours contacter votre administrateur.'))
    return native_write(self, vals)


@api.multi
def unlink(self):
    if self._name in ['sale.order'] and self.env.user.company_id.inventory_inprogress:
        raise AccessError(_('Un inventaire est en cours contacter votre administrateur.'))
    return native_unlink(self)


BaseModel.create = create
BaseModel.write = write
BaseModel.unlink = unlink
