# -*- coding: utf-8 -*-
{
    'name': "新智联图书馆",

    'summary': """
        以读者为中心，以服务为主导""",

    'description': """
        This module is writing for who wants learn odoo developments.
    """,

    'author': "Mr.Lu",
    'website': "http://www.newlink-sz.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'tutorial',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/client.xml',
        'views/views.xml',
        'views/inherit_view.xml'
        # 'views/templates.xml',
    ],
    "qweb":[
        "static/src/xml/page.xml"
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    "application": True
}