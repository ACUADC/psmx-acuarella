from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    logistic_route = fields.Char()
