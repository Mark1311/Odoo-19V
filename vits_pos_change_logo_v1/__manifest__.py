# -*- coding: utf-8 -*-
###############################################################################
# Author      : Varanval IT Solutions
# Copyright   : (c) 2025 Varanval IT Solutions. All Rights Reserved.
#
# This software and associated files are the copyrighted property of Varanval IT Solutions.
# Unauthorized copying, redistribution, or modification of any part of this code
# is strictly prohibited unless expressly permitted by the author.
#
# This module is a paid product. It is licensed for use only by the customer
# who has purchased it, and only for the number of users specified at purchase.
#
# For licensing inquiries, contact: markvaranval@gmail.com
###############################################################################
{
    'name': 'POS Screen Logo | POS Logo | Change POS Logo',
    'version': '19.1.1',
    'category': 'Point of Sale',
    'sequence': 1,
    'summary': "Change POS logo to company logo | POS screen logo customization | Company logo on POS screen and receipt | Replace default POS logo Odoo | POS receipt branding | POS interface logo change | Custom logo in Odoo POS | POS branding and customization | Display company logo in POS | Update POS logo in Odoo",
    'description': """Easily replace the default POS logo in Odoo with your official company logo. 
            Upload your logo from POS settings to instantly display it on both the POS screen and printed receipts for a consistent, professional brand identity. 
            This module helps enhance brand recognition, build customer trust, and give your POS a polished, corporate look. 
            Ideal for retail stores, restaurants, and multi-outlet businesses that want a unified branding experience at every sale. 
            Seamless integration with Odoo 18 POS — simple to configure, no technical skills required, and changes apply instantly in the next POS session.""",
    'depends': ['base', 'point_of_sale', 'stock'],
    'keywords': [
        'pos',
        'pos logo',
        'change pos logo',
        'company logo in pos',
        'pos screen logo',
        'pos receipt logo',
        'odoo pos logo change',
        'custom pos logo',
        'pos branding',
        'pos company branding',
        'pos interface logo',
        'update pos logo',
        'pos logo customization',
        'pos logo changer',
        'replace pos logo',
        'pos screen customization',
        'pos receipt customization',
        'odoo pos customization',
        'odoo pos',
        'odoo',
        'point of sale logo',
        'point of sale company logo',
        'pos logo display',
        'pos header logo',
        'pos printed receipt logo'
    ],
    'author': 'Varanval IT Solutions',
    'company': 'Varanval IT Solutions',
    'price': '3.00',
    'currency': 'USD',
    'data': [
        'views/res_config_settings.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'vits_pos_change_logo_v1/static/src/xml/inherit_receipt_header.xml',
            'vits_pos_change_logo_v1/static/src/xml/inherit_navbar.xml',
            'vits_pos_change_logo_v1/static/src/js/pos_store.js',
            'vits_pos_change_logo_v1/static/src/js/inherit_receipt_header.js',
        ],
    },
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'OPL-1',
}
