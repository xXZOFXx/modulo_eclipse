# -*- coding: utf-8 -*-
{
    'name': "modulo_eclipse",

    'summary': """
        Este es el primer modulo creado en odoo 12 por Eclipse!!""",

    'description': """
        Long description of module's purpose
    """,

    'author': "eclipsemex",
    'website': "http://www.eclipsemex.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Probando modulos ',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
