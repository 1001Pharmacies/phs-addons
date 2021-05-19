from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    street = fields.Char(required=True)
    ref = fields.Char(required=True)
    city = fields.Char(required=True)
    state_id = fields.Many2one(required=True)
    zip = fields.Char(required=True)
    vat = fields.Char(required=True)
    lang = fields.Selection(required=True)
    country_id = fields.Many2one(required=True)
