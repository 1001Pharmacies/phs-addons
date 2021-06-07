/**
 * Copyright 2020 Pharmasimple (http://www.pharmasimple.com)
 * License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
 */

import {process_registry} from "/shopfloor_mobile_base/static/wms/src/services/process_registry.js";

// Clone the original component
const MultiBarcodeClusterBatchPicking = process_registry.extend(
    "cluster_batch_picking",
    {
        // `extend` accepts a path to the final key
        "methods.find_move_line": function (move_lines, barcode, filter = () => true) {
            let move_line;

            move_lines.filter(filter).forEach((line) => {
                if (
                    line.product.barcode === barcode ||
                    line.product.barcodes.map(({name}) => name).includes(barcode)
                ) {
                    move_line = move_line !== undefined ? move_line : line;
                }
            });

            return move_line || {};
        },
    }
);

// Replace process component
process_registry.replace("cluster_batch_picking", MultiBarcodeClusterBatchPicking);
