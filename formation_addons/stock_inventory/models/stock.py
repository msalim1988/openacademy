# -*- coding: utf-8 -*-
from odoo import api, fields, models


class StockInventory(models.Model):
    _inherit = 'stock.inventory'

    @api.multi
    def prepare_inventory(self):
        self.env.user.company_id.write({'inventory_inprogress': True})
        return super(StockInventory, self).action_start()

    @api.multi
    def action_done(self):
        self.env.user.company_id.write({'inventory_inprogress': False})
        return super(StockInventory, self).action_done()

    @api.multi
    def action_cancel_draft(self):
        self.env.user.company_id.write({'inventory_inprogress': False})
        return super(StockInventory, self).action_cancel_draft()
