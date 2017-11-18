# -*- coding: utf-8 -*-
{
    'name' : 'Formation Stock',
    'version' : '1.1',
    'summary': 'Add some improvments to Stock/Inventory',
    'sequence': 0,
    'description': """
Stock /I nventory
====================
    """,
    'category': 'Stock',
    'website': '',
    'images' : [],
    'depends' : ['base', 'stock'],
    'data': [
        # views
        'views/res_company_view.xml',
    ],
    'demo': [
    ],
    'qweb': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
