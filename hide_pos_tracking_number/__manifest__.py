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
    'name': 'Hide Tracking Number on Receipt',
    'version': '19.1.1',
    'category': 'Point of Sale',
    'sequence': 1,
    'summary': "POS Hide Tracking Number | POS Hide Order Number on POS Receipt | Hide tracking details on POS receipts | POS receipt customization | Odoo POS receipt management | Clean POS receipts | Hide sensitive information on POS | POS receipt control | Professional POS receipt layout | POS receipt settings | Odoo POS module | POS receipt toggle | Easy POS customization | POS receipt optimization",
    'description': """Easily control the visibility of tracking numbers and order numbers on POS receipts with this Odoo 18 module. Enable or disable the "Hide Tracking Number" and "Hide Order Number" options from POS settings to customize receipt display instantly. Simplify receipt management, maintain clean and professional-looking receipts, and enhance POS workflow efficiency. Perfect for retail, restaurants, and fast-moving POS operations. Seamless integration with Odoo 18 ensures hassle-free setup and operation while improving customer experience and operational clarity.""",
    'depends': ['base', 'stock', 'point_of_sale'],
    'keywords': [
        'POS',
        'POS hide tracking number',
        'POS hide order number',
        'POS receipt customization',
        'Odoo POS receipt',
        'POS receipt settings',
        'Odoo 19 POS module',
        'POS receipt control',
        'POS receipt toggle',
        'POS receipt optimization',
        'Odoo POS customization',
        'POS receipt management',
        'Professional POS receipts',
        'POS receipt layout',
        'POS workflow efficiency',
        'Retail POS Odoo',
        'Restaurant POS Odoo',
        'Fast-moving POS receipts',
        'Clean POS receipt',
        'POS receipt toggle Odoo'
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
            'hide_pos_tracking_number/static/src/xml/inherit_receipt_header.xml',
        ],
    },
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'OPL-1',
}
