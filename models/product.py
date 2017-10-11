from odoo import api
from odoo import fields
from odoo import models

class product_template(models.Model):
    _inherit="product.template"
    
    is_equipment = fields.Boolean(string="Is an equipment")