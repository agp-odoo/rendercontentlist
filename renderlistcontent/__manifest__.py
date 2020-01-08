# -*- coding: utf-8 -*-
{
    'name': "Render List Content",
    'description': "A widget that renders all content.",
    'summary': """
        This module holds a relational widget called 'render_list_content'. 
        It renders content with URLs accordingly: 
            - Webpages are rendered with the content listed in their meta tags.
            - Images are rendered with image tags.
            - Videos are rendered with video tags.
        The URL must start with an 'http://' or 'https://' for it to be valid.
    """,

    'author': "Odoo",
    'website': "https://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'license': 'AGPL-3',
    'category': 'Render List Content',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': ['assets.xml'],
    
    'qweb': [
        'static/src/xml/render_list_content.xml',
    ]
}
