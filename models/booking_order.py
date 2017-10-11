from odoo import api
from odoo import fields
from odoo import models
from odoo import _
from odoo.exceptions import ValidationError

class booking_order(models.Model):
    
    _name="booking.order"
    _inherits = {  'hasmicro.team': 'hs_team_id'   }
    
    hs_dummy_team_id = fields.Many2one('hasmicro.team',string="Team",) 
    hs_team_id = fields.Many2one('hasmicro.team',string="Team",)
    booking_start = fields.Datetime(string="Booking Start",)
    booking_end= fields.Datetime(string="Booking End",)
    sale_order_id = fields.Many2one('sale.order',string="Sale Order")

    @api.onchange('hs_team_id')
    def onchange_hs_team_id(self):
        if self.hs_team_id:
            self.hs_team_leader_id=self.hs_team_id.hs_team_leader_id
            self.hs_employee_ids=self.hs_team_id.hs_employee_ids
            self.hs_equipment_ids = self.hs_team_id.hs_equipment_ids
            
    @api.onchange('booking_start')
    def onchange_booking_start(self):
        if self.booking_start:
            self.booking_end=(datetime.strptime(self.booking_start,DTF) + relativedelta(hours=+1)).strftime(DTF)    
    

    @api.multi
    def check_booking_overlap(self,extra_args):
        
        self.env.cr.execute("select id from booking_order where id != %s and booking_start between %s and %s\
                             or id != %s and  booking_end between %s and %s",
                             (self.id,self.booking_start,self.booking_end,self.id,self.booking_start,self.booking_end))
        temp_target_ids = [x[0] for x in self.env.cr.fetchall()]
        base_args=[('id','in',temp_target_ids)]
        args=base_args + extra_args
        overlap_sig = self.search(args)
        return overlap_sig
        
#     @api.constrains('hs_team_leader_id')
    def _check_team_leader_book_overlap(self):
        target_data=[x.id for x in self.hs_team_leader_id]
        extra_args=[('hs_team_leader_id','in',target_data)]
        res =  self.check_booking_overlap(extra_args)
        temp_res=[]
        for x in res:
            if x.hs_team_leader_id.id in target_data:
                temp_res.append('Team leader: %s' % x.hs_team_leader_id.name)
        return list(set(temp_res))
    
#     @api.constrains('hs_employee_ids')
    def _check_employees_book_overlap(self):
        target_data=[x.id for x in self.hs_employee_ids]
        extra_args=[('hs_employee_ids','in',target_data)]
        res = self.check_booking_overlap(extra_args)
        temp_res=[]
        for x in res:
            for y in x.hs_employee_ids :
                if y.id in target_data:
                    temp_res.append('Employee: %s' % y.name)
        return list(set(temp_res))
            
#     @api.constrains('hs_equipment_ids')
    def _check_equipments_book_overlap(self):
        target_data=[x.id for x in self.hs_equipment_ids]
        extra_args=[('hs_equipment_ids','in',target_data)]
        res = self.check_booking_overlap(extra_args)
        temp_res=[]
        for x in res:
            for y in x.hs_equipment_ids :
                if y.id in target_data:
                    temp_res.append('Equipment: %s' % y.name)
        return list(set(temp_res))
            
    @api.multi
    def check_booking_order(self):
        team_leader_overlap = self._check_team_leader_book_overlap()        
        employees_overlap = self._check_employees_book_overlap()
        equipment_overlap = self._check_equipments_book_overlap()

        
        base_str=' has an event on that day and time.'
        temp_list=[]
        for x in [team_leader_overlap,employees_overlap,equipment_overlap]:
            if x:
                temp_list+=x

        if temp_list:
            raise ValidationError(_(" and ".join([", ".join(temp_list[:-1]),temp_list[-1]])+base_str))
        
    @api.multi
    def validate_booking_order(self):
        print 'validate_booking_order'