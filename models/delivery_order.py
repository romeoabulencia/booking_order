from odoo import api
from odoo import fields
from odoo import models

class stock_picking(models.Model):
    _inherit = 'stock.picking'
    _inherits = {  'stock.picking': 'booking_id'   }
    
    is_booking = fields.Boolean(string="Is a booking")
    booking_id = fields.Many2one('booking.order',string="Booking")