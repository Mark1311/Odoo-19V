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
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    pos_hide_show_invoice_button = fields.Boolean(string="Pos Hide Invoice Button",
                                                  related="pos_config_id.pos_hide_show_invoice_button",
                                                  readonly=False)
