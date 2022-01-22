from odoo import models, fields


class Neighborhood(models.Model):  # inherit from models.Model
    _name = 'hmisinteg.neighborhood'
    _description = "HMIS Neighborhood"

    district_code = fields.Char(string="District Code", required=True)
    code = fields.Char(string="Neighborhood Code", required=True)
    name = fields.Char(string="English Name", required=True)
    name_arabic = fields.Char(string="Arabic Name", required=True)
    active = fields.Boolean(string="Active", default=True)
    district_id = fields.Many2one('hmisinteg.district',
                                  ondelete='cascade', string="District", required=True)

    _sql_constraints = [
        ('code_unique', 'unique (district_code,code)', 'Code must be unique.')
    ]

