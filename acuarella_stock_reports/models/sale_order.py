from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    logistic_route = fields.Selection(
        [("blue_logistic", "Blue Logistic"),
         ("coord_with_coll", "Coordination with collection"),
         ("coord_wo_coll", "Coordination without collection"),
         ("returns", "Returns"),
         ("address_with_coll", "Address with collection"),
         ("address_wo_coll", "Address without collection"),
         ("dropship", "Dropshipping"),
         ("san_lucas_delivery", "San Lucas's Stores Delivery"),
         ("deliver_with_coll", "Deliver with collection"),
         ("deliver_wo_coll", "Delivery without collection"),
         ("interr_with_coll", "Interrapidismo with collection"),
         ("interr_wo_coll", "Interrapidisimo without collection"),
         ("high_traffic", "High traffic counter"),
         ("pickup", "Pick-up"),
         ("servientrega", "Servientrega"),
         ("san_lucas_cod", "San Lucas Store Cash on delivery"),
         ("san_lucas_wo_coll", "San Lucas Store without collection"),
         ("vanaga", "Vanaga")]
    )
