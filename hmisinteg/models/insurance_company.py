from odoo import models, fields


class InsuranceCompany(models.Model):
    _name = 'hmisinteg.insurance_company'
    _description = "Insurance Company"
    company_id = fields.Integer(string="Odoo Company Id", required=True)
    code = fields.Char(string="Insurance Company Code", required=True)
    name = fields.Char(string="English Name", required=True)
    name_arabic = fields.Char(string="Arabic Name", required=True)
    insurance_mother_company_id = fields.Many2one('hmisinteg.insurance_mother_company',
                                                  ondelete='cascade', string="Mother Company", required=True)
    financial_category_ids = fields.One2many(
        'hmisinteg.financial_category', 'insurance_company_id', string="Financial Categories")
    active = fields.Boolean(string="Active", default=True)

