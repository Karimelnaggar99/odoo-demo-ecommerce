# -*- coding: utf-8 -*-

{
    # Module Information
    'name': 'Website Order Comment | Order Note',
    'category': 'Website/eCommerce',
    'summary': 'Allow user to add order Note/Comment while place the order',
    'version': '16.0.0.0',
    "description": """
        Website Order Note,
        Website Order Comment,
        
    """,
    'license': 'OPL-1',    
    'depends': ['website_sale'],

    'data': [
        'templates/template.xml',
        'view/res_config.xml',
        'view/sale_order.xml',
    ],
    'assets':{
        'web.assets_frontend':[
        '/website_order_note_av/static/src/js/website_order_note.js',
        ]
    },

    #Odoo Store Specific
    'images': [
        'static/description/website_order_note.png',
    ],

    # Author
    'author': 'AV Technolabs',
    'website': 'http://avtechnolabs.com',
    'maintainer': 'AV Technolabs',

    # Technical
    'installable': True,
    'auto_install': False,
    'price': 00,
    "live_test_url":'',
    'currency': 'EUR', 
}
