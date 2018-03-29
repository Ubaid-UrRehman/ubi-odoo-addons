# -*- coding: utf-8 -*-
{
    'name': "Invoice Date Range filter",

    'summary': """
        Add date fields in Invoice and allow to filter base on these dates.""",

    'description': """
        Add date fields in Invoice and allow to filter base on these dates.
    """,

    'author': "Ubaid ur Rehman",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '10.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/sale_config_setting.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}