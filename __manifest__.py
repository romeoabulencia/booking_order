# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': "Booking Service",
    'summary': """
        Booking Service""",
    'version': '1.0',
    'category': 'Uncategorized',
    'license': 'AGPL-3',
    'installable': True,
    'author':'Romeo Abulencia',
    'depends': [
        'hr',
        'product',
        'stock',
        'calendar',
        'sale',
        'delivery',
        
    ],
    'data': [
       
        #product view alterations
        'views/product_views.xml',
        
        #calendar event view alterations
        'views/calendar_event_views.xml',
        
        #employee view alterations
        'views/employee_views.xml',        

        #serial number view alterations
        'views/serial_number_views.xml',
        
        #booking order views
        'views/booking_order_views.xml',
        
        #work order views
        'views/work_order_views.xml',
        
        #deliver order views
        'views/deliver_order_views.xml',
        
        #team views
        'views/team_views.xml',
        
        #menus
        'views/menus.xml',

    ],
}
