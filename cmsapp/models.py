#coding:utf-8
from django.db import models


class Houses(models.Model):
    hid=models.AutoField(primary_key=True)
    saler=models.CharField(max_length=15,verbose_name=u'卖家姓名')
    saler_mobile=models.CharField(max_length=11,verbose_name=u'卖家手机')
    saler_tel = models.CharField(max_length=8, verbose_name=u'卖家座机')
    living_area = models.CharField(max_length=50, verbose_name=u'出售楼盘名')
    BUILDING_NUMBER_CHOICES=(
        (1,'1栋'),(2,'2栋'),(3,'3栋'),(4,'4栋'),(5,'5栋'),(6,'6栋'),(7,'7栋'),(8,'8栋'),(9,'9栋'),(10,'10栋'),
        (11, '11栋'), (12, '12栋'), (13, '13栋'), (14, '14栋'), (15, '15栋'), (16, '16栋'), (17, '17栋'), (18, '18栋'), (19, '19栋'), (20, '20栋'),
        (21, '21栋'), (22, '22栋'), (23, '23栋'), (24, '24栋'), (25, '25栋'), (26, '26栋'), (27, '27栋'), (28, '28栋'),(29, '29栋'), (30, '30栋'),
    )
    FLOOR_NUMBER_CHOICES = (
        (1, '1层'), (2, '2层'), (3, '3层'), (4, '4层'), (5, '5层'), (6, '6层'), (7, '7层'), (8, '8层'), (9, '9层'), (10, '10层'),
        (11, '11层'), (12, '12层'), (13, '13层'), (14, '14层'), (15, '15层'), (16, '16层'), (17, '17层'), (18, '18层'),
        (19, '19层'), (20, '20层'),(21, '21层'), (22, '22层'), (23, '23层'), (24, '24层'), (25, '25层'), (26, '26层'), (27, '27层'), (28, '28层'),
        (29, '29层'), (30, '30层'),(31, '31层'), (32, '32层'), (33, '33层'), (34, '34层'), (35, '35层'), (36, '36层'), (37, '37层'), (38, '38层'),
    )
    ROOM_NUMBER_CHOICES=(
        (1, '1号'), (2, '2号'), (3, '3号'), (4, '4号'), (5, '5号'), (6, '6号'), (7, '7号'), (8, '8号'), (9, '9号'), (10, '10号'),
        (11, '11号'), (12, '12号'), (13, '13号'), (14, '14号'), (15, '15号'), (16, '16号'), (17, '17号'), (18, '18号'),
        (19, '19号'), (20, '20号'),
    )
    DECORATION_CHOICES=(
        (1,'清水'),(2,'简装'),(3,'精装'),
    )
    HOUSE_TYPE_CHOICES=(
        (1,'高层'),(2,'洋房'),(3,'矮层'),(4,'联排'),(5,'独栋'),(6,'不带电梯洋房'),(7,'不带电梯矮层'),
    )
    REGION_CHOICES=(
        (1,'江北区'),(2,'南岸区'),(3,'九龙坡区'),(4,'渝中区'),(5,'大渡口区'),(7,'巴南区'),(8,'渝北区'),(9,'北碚区'),
    )
    LOAN_CHOICES=(
        (1,'贷款'),(2,'全款')
    )
    building_number = models.IntegerField(verbose_name=u'房产栋号',choices=BUILDING_NUMBER_CHOICES)
    floor_number = models.IntegerField(verbose_name=u'楼层',choices=FLOOR_NUMBER_CHOICES)
    room_number = models.IntegerField(verbose_name=u'房号',choices=ROOM_NUMBER_CHOICES)
    decoration=models.IntegerField(verbose_name=u'装修情况',choices=DECORATION_CHOICES)
    room_size=models.IntegerField(verbose_name=u'建筑面积',default=0)
    room_type=models.CharField(max_length=50,verbose_name=u'户型描述')
    house_type=models.IntegerField(verbose_name=u'房产类型',choices=HOUSE_TYPE_CHOICES)
    region=models.IntegerField(verbose_name=u'行政区',choices=REGION_CHOICES)
    building_addr=models.CharField(max_length=200,verbose_name=u'楼盘具体地址')
    house_owner= models.CharField(max_length=11, verbose_name=u'房产归属人')
    buy_time=models.DateField(verbose_name=u'房产购买时间')
    building_time=models.DateField(verbose_name=u'楼盘开盘时间')
    is_loan=models.IntegerField(verbose_name=u'是否贷款',choices=LOAN_CHOICES)
    sale_price=models.FloatField(verbose_name=u'售价')

    class Meta:
        db_table='Houses'
        verbose_name='房产信息'
        verbose_name_plural=verbose_name


class Customers(models.Model):
    cid=models.AutoField(primary_key=True)
    customer_name=models.CharField(max_length=15,verbose_name=u'客户名')
    customer_mobile = models.CharField(max_length=11, verbose_name=u'客户手机')
    intention=models.ManyToManyField(Houses,verbose_name=u'意向房产')
    is_look=models.IntegerField(default=0,verbose_name=u'是否看房')#0 没有看  1 已经看过
    look_time=models.DateTimeField(verbose_name=u'最后看房时间',default=None)
    is_deal=models.IntegerField(default=0,verbose_name=u'是否成交')#0 没有  1 已经成交
    deal_contract=models.ImageField(max_length=500,verbose_name=u'合同信息')
    class Meta:
        db_table='Customers'
        verbose_name='客源信息'
        verbose_name_plural=verbose_name