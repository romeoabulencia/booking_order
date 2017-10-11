from odoo import api
from odoo import fields
from odoo import models

class booking_order(models.Model):
    _name="booking.order"
    _inherits = {  'hasmicro.team': 'hs_team_id'   }
    
    hs_team_id = fields.Many2one('hasmicro.team',string="Team")
#     team_leader_id = fields.Many2one('hr.employee',string="Team Leader")
#     employee_ids = fields.Many2many('hr.employee',string="Employees")
#     equipment_ids= fields.Many2many('product.product',string="Equipments")
    booking_start = fields.Datetime(string="Booking Start",)
    booking_end= fields.Datetime(string="Booking End",)
    sale_order_id = fields.Many2one('sale.order',string="Sale Order")