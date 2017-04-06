#coding:utf-8
import xadmin
from xadmin import views

from cmsapp.models import *

class BaseSetting(object):
    enable_themes=True
    use_bootswatch=True

class GlobalSetting(object):
    site_title="HOUSECMS"
    site_footer="right by simba"
    menu_style="accordion"


class HousesAdmin(object):
    list_display = ['saler','saler_mobile','living_area','building_number','floor_number','room_number','decoration','room_size','room_type','house_type','building_addr']
    search_fields = ['saler']
    list_filter = ['saler']


class CustomersAdmin(object):
    list_display=['customer_name','customer_mobile','intention','is_look','look_time','is_deal','deal_contract']
    search_fields=['customer_name','customer_mobile','intention','deal_contract']
    list_filter = ['customer_name','customer_mobile','intention','is_look','deal_contract']


xadmin.site.register(Houses,HousesAdmin)
xadmin.site.register(Customers,CustomersAdmin)

xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSetting)