# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'frotaweb',
    'version': '0.1',
    'summary': 'Main module',
    'depends': [
        'base_setup',
        'sales_team',
        'mail',
        'calendar',
        'resource',
        'fetchmail',
        'utm',
        'web_tour',
        'contacts',
        'digest',
        'phone_validation',
    ],
    'auto_install': True,
    'application': True,
    'installable': True
}