from datetime import datetime

from odoo import models, fields, api


class Patient(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    name = fields.Char(index=True, required=False)
    name_first_english = fields.Char(string="Name First English", required=True)
    name_second_english = fields.Char(string="Name Second English", required=True)
    name_third_english = fields.Char(string="Name Third English", required=True)
    name_fourth_english = fields.Char(string="Name Fourth English", required=True)

    name_arabic = fields.Char(string="Arabic Name")
    name_first_arabic = fields.Char(string="Name First Arabic", required=True)
    name_second_arabic = fields.Char(string="Name Second Arabic", required=True)
    name_third_arabic = fields.Char(string="Name Third Arabic", required=True)
    name_fourth_arabic = fields.Char(string="Name Fourth Arabic", required=True)

    phone = fields.Char(string="Mobile")
    mobile = fields.Char(string="Phone")

    date_of_birth = fields.Date(string="Date of Birth")
    gender = fields.Selection([
        ('M', 'Male'),
        ('F', 'Female'),
    ], required=True, default='M')
    # gender = fields.Char(string="Gender")
    facebook = fields.Char(string="Facebook")
    instagram = fields.Char(string="Instagram")
    linkedin = fields.Char(string="LinkedIn")

    last_financial_category_id = fields.Many2one('hmisinteg.financial_category',
                                                 string="Last Financial Category")
    integ_line_status = fields.Char(string="Updated", default='N')  # don't display it
    patient_number = fields.Integer(string="Patient Number")  # not editable
    # address part
    integ_country_id = fields.Many2one('hmisinteg.country', string="HMIS Country")  # Country
    integ_city_id = fields.Many2one('hmisinteg.city', string="HMIS City")  # Governorate
    integ_district_id = fields.Many2one('hmisinteg.district', string="HMIS District")  # City
    integ_neighborhood_id = fields.Many2one('hmisinteg.neighborhood', string="HMIS Neighborhood")  # District

    @api.model
    def create(self, vals):
        self.name_arabic = ' '
        vals['name_arabic'] = vals.get('name_fourth_arabic') + ' ' + vals.get('name_third_arabic') + ' ' + vals.get(
            'name_second_arabic') + ' ' + vals.get('name_first_arabic')
        self.name = ' '
        vals['name'] = vals.get('name_first_english') + ' ' + vals.get('name_second_english') + ' ' + vals.get(
                'name_third_english') + ' ' + vals.get('name_fourth_english')
        res = super(Patient, self).create(vals)
        return res

    # @api.model
    # def create(self, vals):
    #     name = ' '
    #     if vals.get('name_first_english'):
    #         name += ' ' + vals['name_first_english']
    #     if vals.get('name_second_english'):
    #         name += ' ' + vals['name_second_english']
    #     if vals.get('name_third_english'):
    #         name += ' ' + vals['name_third_english']
    #     if vals.get('name_fourth_english'):
    #         name += ' ' + vals['name_fourth_english']
    #     vals['name'] = name
    #     res = super(Patient, self).create(vals)
    #     return res

    # @api.depends('name_first_arabic', 'name_second_arabic', 'name_third_arabic', 'name_fourth_arabic')
    # def comp_arabic_name(self):
    #     self.name_arabic = (self.name_first_arabic or '') + ' ' + (self.name_second_arabic or '') + ' ' + (
    #             self.name_third_arabic or '') + ' ' + (self.name_fourth_arabic or '')
    #
    # @api.depends('name_first_english', 'name_second_english', 'name_third_english', 'name_fourth_english')
    # def comp_english_name(self):
    #     self.name = (self.name_first_english or '') + ' ' + (self.name_second_english or '') + ' ' + (
    #             self.name_third_english or '') + ' ' + (self.name_fourth_english or '')

    # @api.model_create_multi
    # def create(self, vals_list):
    #     new_id = super(Patient, self).create(vals_list)
    #     self.name_arabic = "%s %s %s %s" % (self.name_first_arabic, self.name_second_arabic, self.name_third_arabic, self.name_fourth_arabic)
    #     print(self.name_arabic)
    #     return new_id
