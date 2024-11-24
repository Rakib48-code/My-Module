{
    'name': 'My Module',
    'version': '1.0',
    'category': 'Uncategorized',
    'summary': 'A short description of what your module does.',
    'description': """
        A detailed description of your module. 
        This section can include instructions on usage and any other relevant details.
    """,
    'depends': ['base'],  # List other Odoo modules that your module depends on
    'data': [
        # Add XML files, views, data files, security rules, etc.
        'security/ir.model.access.csv',
        'views/menu_view.xml',
        'views/course_menu.xml',

    ],
    'demo':[
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
