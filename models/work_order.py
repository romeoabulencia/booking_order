from odoo import api
from odoo import fields
from odoo import models

class work_order(models.Model):
    _name="work.order"
    _inherits = {  'hasmicro.team': 'team_id'   }
    
    booking_id = fields.Many2one('booking.order',strting="Booking")
    scheduled_start = fields.Date('Scheduled Date')
    scheduled_end = fields.Date('Scheduled End')
    actual_start = fields.Date('Actual Start')
    actual_end = fields.Date('Actual End')
    hs_team_id = fields.Many2one('hasmicro.team',string="Team")
#     team_leader_id = fields.Many2one('hr.employee',string="Team Leader")
#     employee_ids = fields.Many2many('hr.employee',string="Employees")
#     equipment_ids= fields.Many2many('product.product',string="Equipments")