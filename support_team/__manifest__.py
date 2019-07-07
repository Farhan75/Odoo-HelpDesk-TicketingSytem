# -*- coding: utf-8 -*-
# © 2017 Dave Burkholder <dave@thinkwelldesigns.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Support Teams',
    'version': '1.0',
    'category': 'Support',
    'summary': 'Manage Support Teams on Issues & Tasks',
    'author': "Thinkwell Designs",
    'website': "http://www.thinkwelldesigns.com",

    'depends': [
        'crm',
        'sales_team',
        'project_issue',
    ],
    'data': [
        'security/support_team.xml',
        'views/crm.xml',
        'views/project_project.xml',
        'views/support_team.xml',
        'views/project_task.xml',
        'views/project_issue.xml',
     ],
    'installable': True,
    'auto_install': False,
}
