# -*- coding: utf-8 -*-

import logging
import os
import random
import requests

from odoo import http, models, fields, api, _
from odoo.http import request
from werkzeug.utils import redirect
from urllib.parse import quote
from odoo.exceptions import UserError

logger = logging.getLogger(__name__)


class CustomAuthLogout(http.Controller):
    # Default Odoo login logic
    @http.route('/web/session/logout', type='http', auth="user", website=True)
    def logout(self, **kwargs):
        request.session.logout()
        base_url = request.httprequest.host_url
        post_logout_redirect_uri = f"{base_url}web/login"
        encoded_redirect_uri = quote(post_logout_redirect_uri, safe='')
        auth0_logout_url = f"https://auth.pinme.io/oidc/logout?post_logout_redirect_uri={encoded_redirect_uri}"

        return redirect(auth0_logout_url, 303)


class Frotaweb(http.Controller):
    @http.route('/frotaweb/statistics', type='json', auth='user')
    def get_statistics(self):
        """
        Returns a dict of statistics about the orders:
            'average_quantity': the average number of t-shirts by order
            'average_time': the average time (in hours) elapsed between the
                moment an order is created, and the moment is it sent
            'nb_cancelled_orders': the number of cancelled orders, this month
            'nb_new_orders': the number of new orders, this month
            'total_amount': the total amount of orders, this month
        """

        return {
            'average_quantity': random.randint(4, 12),
            'average_time': random.randint(4, 123),
            'nb_cancelled_orders': random.randint(0, 50),
            'nb_new_orders': random.randint(10, 200),
            'orders_by_size': {
                'm': random.randint(0, 150),
                's': random.randint(0, 150),
                'xl': random.randint(0, 150),
            },
            'total_amount': random.randint(100, 1000)
        }


class MaintenanceEquipment(models.Model):
    _inherit = 'maintenance.equipment'

    serial_no = fields.Char(
        required=True
    )

    @api.model
    def create(self, vals):
        record = super(MaintenanceEquipment, self).create(vals)
        try:
            self._create_traccar(vals)
        except UserError as e:
            record.unlink()
            raise e
        return record

    def _create_traccar(self, vals):
        user = self.env.user
        traccar_url = os.environ.get('TRACCAR_URL')
        if not traccar_url:
            raise UserError("Tracking server URL is not configured")

        if not user.traccar_token:
            raise UserError("The current user is not configured.")

        headers = {
            "Authorization": f"Bearer {user.traccar_token}",
            "Content-Type": "application/json",
        }
        response = requests.post(f"{traccar_url}/api/devices",
                                 json={"uniqueId": vals.get("serial_no"), "name": vals.get("name")},
                                 headers=headers)

        if response.status_code != 200:
            raise UserError(_("Another asset already exists with this serial number!"))
