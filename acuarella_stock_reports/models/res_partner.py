from odoo import models


class ResPartner(models.Model):
    _inherit = "res.partner"

    def _display_address(self, without_company=False):
        return super()._display_address(
            without_company=self._context.get('force_without_company') or without_company
        )
