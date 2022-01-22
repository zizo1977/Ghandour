from odoo import models, fields


class District(models.Model):  # inherit from models.Model
    _name = 'hmisinteg.district'
    _description = "HMIS District"

    city_code = fields.Char(string="City Code", required=True)
    code = fields.Char(string="District Code", required=True)
    name = fields.Char(string="English Name", required=True)
    name_arabic = fields.Char(string="Arabic Name", required=True)
    active = fields.Boolean(string="Active", default=True)
    city_id = fields.Many2one('hmisinteg.city',
                              ondelete='cascade', string="City", required=True)
    neighborhood_ids = fields.One2many(
        'hmisinteg.neighborhood', 'district_id', string="Neighborhoods")
    _sql_constraints = [
        ('code_unique', 'unique (city_code,code)', 'Code must be unique.')
    ]


