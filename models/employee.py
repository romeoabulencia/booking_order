from odoo import api
from odoo import fields
from odoo import models

class hr_employee(models.Model):
    _inherit="hr.employee"
    
    @api.multi
    def get_employee_calendar_events(self):
        
        target_user_id = []
        target_partner_id = []
        if self.user_id:
            target_user_id.append(self.user_id.id)
            if self.user_id.partner_id.id:
                target_partner_id.append(self.user_id.partner_id.id) 
        
        #fetch connected events by res_users (calendar event owned)
        event_owner_args=[('user_id','in',target_user_id)]
        calendar_event_ids = self.env['calendar.event'].search(event_owner_args)
        #fetch connected events by res_partner (calendar event attended))
        event_attended_args=[('partner_ids','in',target_partner_id)]
        calendar_event_ids += self.env['calendar.event'].search(event_attended_args)        
        
        return{ 'view_type': 'calendar',
                    'view_mode': 'calendar',
                    'res_model': 'calendar.event',
                    'domain': [('id','in',[x.id for x in calendar_event_ids])],
                    'type': 'ir.actions.act_window',}        