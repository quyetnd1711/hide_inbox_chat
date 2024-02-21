# -*- coding: utf-8 -*-
{
    'name': "Hide Inbox Chat",
    'license': 'AGPL-3',
    'summary': """Hide icon Activity from header""",
    'description': """
        Hide icon inbox chat
    """,
    'version': "17.0",
    'author': "Duc Quyet",
    'support': 'nquyet76@gmail.com',
    'images': ['static/description/icon.png'],
    'category': 'tools',
    'depends': ['base'],
    'data': [

    ],
    'assets': {
        'web.assets_backend': [
            'hide_inbox_chat/static/src/xml/*.xml',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}
