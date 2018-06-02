# -*- coding: utf-8 -*-

{
    'name': 'Invoice Summary Report XLSX',
    'version': '0.1',
    'category': 'Accounting',
    'summary': 'Invoice Analysis Report',
    'license':'LGPL-3',
    'description': """
    Invoice Summary Report
""",
    'author' : 'Ubaid ur Rehman <ubaidur.rehman018@yahoo.com>',
    'depends': ['account'],
    'images': ['static/description/banner.jpg'],
    'data': [
        'wizard/print_invoice_summary_view.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True
}

# vim:expandtab:smartindent:tabstop=2:softtabstop=2:shiftwidth=2:
