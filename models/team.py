from odoo import api
from odoo import fields
from odoo import models

class hasmicro_team(models.Model):
    _name = "hasmicro.team"
    
    name = fields.Char(required=False,string="Team Name")
    hs_team_leader_id = fields.Many2one('hr.employee',string="Team Leader")
    hs_employee_ids = fields.Many2many('hr.employee','team_employees_rel','team_id','employee_id',string="Employees")
    hs_equipment_ids = fields.Many2many('stock.production.lot',string="Equipments")