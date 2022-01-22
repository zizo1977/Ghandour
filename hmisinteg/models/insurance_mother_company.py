from odoo import models, fields


class InsuranceMotherCompany(models.Model):  # inherit from models.Model
    _name = 'hmisinteg.insurance_mother_company'
    _description = "Insurance Mother Company"

    company_id = fields.Integer(string="Odoo Company Id", required=True)
    code = fields.Char(string="Insurance Company Code", required=True)
    name = fields.Char(string="English Name", required=True)
    name_arabic = fields.Char(string="Arabic Name", required=True)
    insurance_company_ids = fields.One2many(
        'hmisinteg.insurance_company', 'insurance_mother_company_id', string="Insurance Companies")
    active = fields.Boolean(string="Active", default=True)

