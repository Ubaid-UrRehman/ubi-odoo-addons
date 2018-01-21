# -*- coding: utf-8 -*-
{
    'name': "Send Email Notification on Password Change",

    'summary': """
        Send email notification when password changes or user created""",

    'description': """
        Send email notification when password changes or user created
    """,

    'author': "Ubaid ur Rehman",
    'website': "http://www.example.com",
    'contributors': ['Ubaid ur Rehman <ubaidur.rehman018@yahoo.com>',
                     ],

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '10.0.1',

    # any module necessary for this one to work correctly
    'depends': ['auth_signup'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
       # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}