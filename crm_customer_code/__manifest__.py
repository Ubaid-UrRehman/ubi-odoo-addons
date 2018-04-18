# -*- coding: utf-8 -*-
{
    'name': "CRM Customer Code",

    'summary': """
        Customer Code in CRM. Check customer exist or not when convert lead to opportunity.""",

    'description': """
        Customer Code in CRM. Check customer exist or not when convert lead to opportunity.
    """,

    'author': "Ubaid ur Rehman",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['crm', 'customer_code'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}