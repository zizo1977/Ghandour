from odoo import models, fields


class FinancialCategory(models.Model):
    _name = 'hmisinteg.financial_category'
    _description = "Financial Category"
    company_id = fields.Integer(string="Odoo Company Id", required=True)
    code = fields.Char(string="Financial Category Code", required=True)
    nature = fields.Char(string="Financial Category Nature", required=True)
    insurance_company_id = fields.Many2one('hmisinteg.insurance_company',
                                           ondelete='cascade', string="Insurance Company", required=True)
    name = fields.Char(string="English Name", required=True)
    name_arabic = fields.Char(string="Arabic Name", required=True)
    active = fields.Boolean(string="Active", default=True)

    patient_ids = fields.One2many(
        'res.partner', 'last_financial_category_id', string="Patients")



