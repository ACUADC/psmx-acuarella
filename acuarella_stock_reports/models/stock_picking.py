from odoo import fields, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    currency_id = fields.Many2one(related="company_id.currency_id")
    charge = fields.Monetary(currency_field="currency_id")
    package_num = fields.Float()
    partner_address = fields.Char("Contact Address", related="partner_id.contact_address")
    partner_phone = fields.Char("Contact Phone", related="partner_id.phone")
    sale_logistic_route = fields.Char(related="sale_id.logistic_route")
