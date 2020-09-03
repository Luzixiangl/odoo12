# -*- coding: utf-8 -*-
{
    'name': "nlbook",

    'summary': """
        新智联图书库 来自于新智联软件技术公司""",

    'description': """
        新智联图书库
    """,

    'author': "New Link From ShenZhen",
    'website': "http://www.newlink-sz.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/templates.xml',
        'views/views.xml',
    ],

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}