from odoo import api, fields, models


class StockPickingBatch(models.Model):
    _inherit = "stock.picking.batch"

    sale_logistic_routes = fields.Char(
        help="Logistic routes from all sale orders related to each transfer separated by comma",
        compute="_compute_sale_logistic_routes",
    )
    supervisor = fields.Char()

    @api.depends('picking_ids.sale_logistic_route')
    def _compute_sale_logistic_routes(self):
        logistic_routes = dict(self.env['stock.picking']._fields['sale_logistic_route']._description_selection(self.env))
        for batch in self:
            logistic_routes = set(logistic_routes[pick.sale_logistic_route] for pick in batch.picking_ids if pick.sale_logistic_route)
            batch.sale_logistic_routes = ", ".join(logistic_routes)
