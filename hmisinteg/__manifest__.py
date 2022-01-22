# -*- coding: utf-8 -*-
{
    'name': 'HMIS Integration',
    'summary': 'HMIS Integration',
    'description': """
        HMIS Integration:
           
    """,
    'author': 'ProTech',
    'website': 'http://www.yourcompany.com',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'crm', 'purchase_stock'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/patient.xml',
        # 'views/hide_inherited_respartner_notebook.xml',
        # 'views/hide_respartner_button.xml',
        # 'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
