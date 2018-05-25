# -*- coding: utf-8 -*-
{
    'name': "采购跟踪1",

    'summary': """
        采购跟踪1""",

    'description': """
        采购跟踪1
    """,

    'author': "TonyLd",
    'website': "malijie.cc",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['web'],
    'images': [],

    # always loaded
    # 注意data中的文件顺序，ref的ID对应的record一定要在前面
    # 不理解的看views.xml中的action和menuitem的定义顺序
    'data': [
        'views/views.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}