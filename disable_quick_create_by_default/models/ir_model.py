from odoo import fields, models


class IrModel(models.Model):
    _inherit = "ir.model"

    avoid_quick_create = fields.Boolean(default=True)
