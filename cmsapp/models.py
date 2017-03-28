#coding:utf-8

from django.db import models


class Houses(models.Model):
    saler=models.CharField(max_length=15,verbose_name=u'卖家姓名')
    saler_mobile=models.CharField(max_length=11,verbose_name=u'卖家手机')
    saler_tel = models.CharField(max_length=8, verbose_name=u'卖家座机')
    saler_mobile = models.CharField(max_length=11, verbose_name=u'卖家手机')
    living_area = models.CharField(max_length=50, verbose_name=u'出售楼盘名')
    address=models.CharField(max_length=200,verbose_name=u'楼盘地址',blank=False)
    building_number = models.IntegerField(max_length=2,verbose_name=u'出售栋号单元号')
    floor_number = models.CharField(max_length=11, verbose_name=u'出售楼层')
    house_number = models.CharField(max_length=11, verbose_name=u'出售房间号')
    house_owner= models.CharField(max_length=11, verbose_name=u'房产归属人')
    is_loan=models.IntegerField(max_length=1,verbose_name=u'是否贷款',default=0)  #0 贷款，1 全款
    decorating=models.CharField(max_length=1,verbose_name=u'装修情况',default=0)  #0 清水 1 简装  2 精装
    sale_price=models.IntegerField(max_length=8,verbose_name=u'售价')
    class Meta:
        db_table='Houses'
        verbose_name='房产信息'
        verbose_name_plural=verbose_name