# Copyright 2020 Camptocamp SA (http://www.pharmasimple.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo.addons.component.core import Component
from odoo.addons.shopfloor_base.utils import ensure_model


class DataAction(Component):
    _inherit = "shopfloor.data.action"

    @ensure_model("product.barcodes")
    def barcodes(self, record, **kw):
        return self._jsonify(record, self._barcodes_parser, **kw)

    def barcodes_list(self, record, **kw):
        return self.barcodes(record, multi=True)

    @property
    def _barcodes_parser(self):
        return [
            "id",
            "name",
        ]

    @property
    def _product_parser(self):
        pp = super(DataAction, self)._product_parser
        pp.append(("barcode_ids:barcodes", self._product_barcodes))
        return pp

    def _product_barcodes(self, rec, field):
        return self._jsonify(
            rec.barcode_ids,
            self._barcodes_parser,
            multi=True,
        )
