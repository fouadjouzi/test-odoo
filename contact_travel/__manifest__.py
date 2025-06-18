{
    'name': 'Contact Travel - par ton prénom',
    'version': '1.0',
    'summary': 'Gestion des voyages liés aux contacts',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/voyage_views.xml',
        'views/partner_views.xml',
    ],
    'application': True,
}