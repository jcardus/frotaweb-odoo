from odoo.addons.portal.controllers.portal import CustomerPortal


class PortalAccount(CustomerPortal):

    def _prepare_portal_layout_values(self):
        # EXTENDS 'portal'
        portal_layout_values = super()._prepare_portal_layout_values()
        return portal_layout_values