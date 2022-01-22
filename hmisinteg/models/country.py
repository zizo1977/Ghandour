from odoo import models, fields


class Country(models.Model):  # inherit from models.Model
    _name = 'hmisinteg.country'
    _description = "HMIS Country"

    code = fields.Char(string="Country Code", required=True)
    name = fields.Char(string="English Name", required=True)
    name_arabic = fields.Char(string="Arabic Name", required=True)
    active = fields.Boolean(string="Active", default=True)
    city_ids = fields.One2many(
        'hmisinteg.city', 'country_id', string="Cities")

    _sql_constraints = [
        ('code_unique', 'unique (code)', 'Code must be unique.')
    ]


