# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from collections import OrderedDict

from odoo import fields, http, _
from odoo.osv import expression
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager
from odoo.addons.account.controllers.download_docs import _get_headers, _build_zip_from_data
from odoo.exceptions import AccessError, MissingError
from odoo.http import request


class PortalAccount(CustomerPortal):

    def _prepare_portal_layout_values(self):
        # EXTENDS 'portal'
        portal_layout_values = super()._prepare_portal_layout_values()
        partner = request.env.user.partner_id        
        return portal_layout_values