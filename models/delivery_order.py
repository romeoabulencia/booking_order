from odoo import api
from odoo import fields
from odoo import models

class stock_picking(models.Model):
    _inherits = {  'booking.order': 'booking_id',
                    'work.order' : 'hs_work_order_id'   }
    _inherit="stock.picking"
    

    
    is_booking = fields.Boolean(string="Is a booking")
    hs_booking_id = fields.Many2one('booking.order',string="Booking")
    hs_work_order_id = fields.Many2one('work.order',string="Work Order")
    #picking_type_code='outgoing'
    
    
#     @api.onchange('hs_dummy_team_id')
#     def onchange_dummy_team_id(self):
#         self.booking_id.onchange_dummy_team_id()
#          
#     
#     @api.onchange('hs_team_id')
#     def onchange_hs_team_id(self):
#         self.booking_id.onchange_hs_team_id() 
