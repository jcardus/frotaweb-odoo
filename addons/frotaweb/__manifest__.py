{
    'name': 'frotaweb',
    'version': '0.1',
    'summary': 'Main module',
    'depends': [
        'account', 'portal', 'auth_oauth', 'auth_oauth_autologin'
    ],
    'auto_install': [],
    'application': True,
    'installable': True,
    'data': [
        'data/oauth_provider_data.xml',
        'views/frotaweb_portal_templates.xml'
    ],
}