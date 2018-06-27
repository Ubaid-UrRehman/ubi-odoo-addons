{
    'name': 'Sign-up Form with Extra Fields',
    'category': 'Website',
    'summary': 'Sign-up Extended Form.',
    'author': 'Ubaid ur Rehman <ubaidur.rehman018@yahoo.com>',
    'version': '1.0',
    'description': """
    
    This module can create users from the Odoo main screen as an external user and sign-up with the same credentials. 
    It mainly provides validation of email-id and mobile number during sign-up. 
    User id has to be  unique for every account so email id and mobile number cannot be duplicated.
    
        """,
    'depends': ['auth_signup'],
    'data': [
        'views/auth_signup_inherit.xml',
    ],
    'images' :  ['static/description/banner.jpg'],
    'installable': True,
    'application': True,
}
