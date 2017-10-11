from odoo import api
from odoo import fields
from odoo import models
from dateutil.relativedelta import relativedelta
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT as DTF
from datetime import datetime




class sale_order(models.Model):
    _name="sale.order"
    _inherits = {  'booking.order': 'booking_id'   }
    _inherit = ['sale.order']
    
    is_booking = fields.Boolean(string="Is a booking")
    booking_id = fields.Many2one('booking.order',string="Booking")
    
    @api.onchange('hs_team_id')
    def onchange_hs_team_id(self):
        if self.hs_team_id:
            self.hs_team_leader_id=self.hs_team_id.hs_team_leader_id
            self.hs_employee_ids=self.hs_team_id.hs_employee_ids
            self.hs_equipment_ids = self.hs_team_id.hs_equipment_ids
            
    @api.onchange('booking_start')
    def onchange_booking_start(self):
        print 'type',type(self.booking_start)
        if self.booking_start:
            self.booking_end=(datetime.strptime(self.booking_start,DTF) + relativedelta(hours=+1)).strftime(DTF)
    
    
     
   