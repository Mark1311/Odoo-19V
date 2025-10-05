/**
 * ###########################################################################
 * Author      : Varanval IT Solutions
 * Copyright   : (c) 2025 Varanval IT Solutions. All Rights Reserved.
 *
 * This JavaScript file is part of a paid Odoo module developed by Varanval IT Solutions.
 *
 * This module is licensed only for use by the customer who has purchased it,
 * and only for the number of users specified at the time of purchase.
 *
 * For licensing inquiries, contact: markvaranval@gmail.com
 * ###########################################################################
 */
import { patch } from "@web/core/utils/patch";
import { ReceiptHeader } from "@point_of_sale/app/screens/receipt_screen/receipt/receipt_header/receipt_header";
import { usePos } from "@point_of_sale/app/store/pos_hook";

patch(ReceiptHeader.prototype, {
    setup() {
        super.setup();
        this.pos = usePos();
    },
});
