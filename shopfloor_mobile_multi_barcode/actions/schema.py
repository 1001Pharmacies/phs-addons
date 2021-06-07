# Copyright 2020 Camptocamp SA (http://www.pharmasimple.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo.addons.component.core import Component


class ShopfloorSchemaAction(Component):
    _inherit = "shopfloor.schema.action"

    def product(self):
        p = super(ShopfloorSchemaAction, self).product()
        p.update(
            {
                "barcodes": self._schema_list_of(self.barcodes()),
            }
        )
        return p

    def barcodes(self):
        return {
            "name": {"type": "string", "nullable": False, "required": True},
        }
