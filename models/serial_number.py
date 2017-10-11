from odoo import api
from odoo import fields
from odoo import models

class stock_production_lot(models.Model):
    _inherit="stock.production.lot"
    
    @api.multi
    def get_serial_number_calendar_events(self):
        
        
        event_args=[('equipment_ids','in',[self.id])]
        calendar_event_ids = self.env['calendar.event'].search(event_args)        
        
        return{ 'view_type': 'calendar',
                    'view_mode': 'calendar',
                    'res_model': 'calendar.event',
                    'domain': [('id','in',[x.id for x in calendar_event_ids])],
                    'type': 'ir.actions.act_window',}        