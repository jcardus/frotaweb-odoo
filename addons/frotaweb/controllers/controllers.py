# -*- coding: utf-8 -*-

import logging
import random

from odoo import http
from odoo.http import request
from werkzeug.utils import redirect
from urllib.parse import quote

logger = logging.getLogger(__name__)


class CustomAuthLogout(http.Controller):
    # Default Odoo login logic
    @http.route('/web/session/logout', type='http', auth="user", website=True)
    def logout(self, **kwargs):
        request.session.logout()
        base_url = request.httprequest.host_url
        post_logout_redirect_uri = f"{base_url}web/login"
        encoded_redirect_uri = quote(post_logout_redirect_uri, safe='')
        auth0_logout_url = f"https://auth.pinme.io/logout?post_logout_redirect_uri={encoded_redirect_uri}"

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

