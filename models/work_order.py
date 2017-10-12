from odoo import api
from odoo import fields
from odoo import models

class work_order(models.Model):
    _name="work.order"
    _inherits = {  'hasmicro.team': 'hs_team_id'   }
    
    booking_id = fields.Many2one('booking.order',strting="Booking")
    scheduled_start = fields.Datetime('Scheduled Datetime',related="booking_id.booking_start")
    scheduled_end = fields.Datetime('Scheduled End',related="booking_id.booking_end")
    actual_start = fields.Datetime('Actual Start')
    actual_end = fields.Datetime('Actual End')
    hs_team_id = fields.Many2one('hasmicro.team',string="Team")


#     @api.onchange('booking_id')
#     def onchange_booking_id(self):
#         if self.booking_id:
#             self.actual_start=self.booking_id.booking_start
#             self.actual_end=self.booking_id.booking_end