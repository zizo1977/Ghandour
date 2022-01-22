from odoo import models, fields


class City(models.Model):  # inherit from models.Model
    _name = 'hmisinteg.city'
    _description = "HMIS City"

    country_code = fields.Char(string="Country Code", required=True)
    code = fields.Char(string="City Code", required=True)
    name = fields.Char(string="English Name", required=True)
    name_arabic = fields.Char(string="Arabic Name", required=True)
    active = fields.Boolean(string="Active", default=True)
    country_id = fields.Many2one('hmisinteg.country',
                                 ondelete='cascade', string="Country", required=True)
    district_ids = fields.One2many(
        'hmisinteg.district', 'city_id', string="Cities")

    _sql_constraints = [
        ('code_unique', 'unique (country_code,code)', 'Code must be unique.')
    ]
