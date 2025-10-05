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
import logging
from odoo import fields, models, api

_logger = logging.getLogger(__name__)


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    company_logo = fields.Binary("POS CompanyLogo", attachment=True)

    @api.model
    def set_values(self):
        super(ResConfigSettings, self).set_values()
        param = self.env['ir.config_parameter'].sudo()
        param.set_param('res.config.settings.company_logo', self.company_logo)

        _logger.info(f"[SET] company_logo = {self.company_logo}")

    def get_values(self):
        res = super().get_values()
        param = self.env['ir.config_parameter'].sudo()

        res.update(
            company_logo=param.get_param('res.config.settings.company_logo'),
        )

        _logger.info(f"[GET] receipt_logo = {self.company_logo}")
        return res
