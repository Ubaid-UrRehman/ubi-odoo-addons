# -*- coding: utf-8 -*-
{
    'name': "Customer Purchased Products",

    'summary': """
        Customer Purchase Products Information""",

    'description': """
        Add a smart button on Customer form to show the total number of products
        purchased by him.
    """,

    'author': "Ubaid ur Rehman",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '10.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/product_template.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}