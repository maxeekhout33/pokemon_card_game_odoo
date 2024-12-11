{
    'name': 'Pokemon_card_game',
    'category': 'Curso',
    'version': '16.0.0.0.0',
    'license': 'AGPL-3',
    'author': 'Iciva Technology',
    'depends': [
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/user.xml',
        'views/card.xml',
        'views/menu.xml',
    ],
    'assets': {
        'web.assets_frontend': [
        ],
    },
    'application': True,
    'installable': True,
}
