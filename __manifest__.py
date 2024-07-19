{
    'name': 'Helpdesk GPT-4 Integration',
    'version': '1.5',
    'category': 'Helpdesk',
    'summary': 'Integrate Helpdesk with GPT-4, support for multi-company, query functionality, automatic knowledge base updates, and access levels',
    'depends': ['helpdesk'],
    'data': [
        'views/helpdesk_ticket_views.xml',
        'views/helpdesk_gpt4_config_settings_views.xml',
        'views/helpdesk_gpt4_query_views.xml',
        'views/helpdesk_gpt4_knowledge_views.xml',
        'security/ir.model.access.csv',
        'security/helpdesk_gpt4_security.xml',
        'data/helpdesk_gpt4_cron.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'maintainers': [],
    'license': 'LGPL-3',
}
