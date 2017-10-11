from odoo import api
from odoo import fields
from odoo import models

class calendar_event(models.Model):
    _inherit="calendar.event"
    
    hs_equipment_ids=fields.Many2many('stock.production.lot',String="Equipments")