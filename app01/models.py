from django.db import models
# python manage.py makemigrations
# python manage.py migrate
# Create your models here.
class Department(models.Model):
    title = models.CharField(verbose_name="部门标题",max_length=32)
    def __str__(self):
        return self.title

class UserInfo(models.Model):
    name = models.CharField(max_length=16)
    password = models.CharField(max_length=64)
    age = models.IntegerField()
    account = models.DecimalField(verbose_name="账户余额",max_digits=10,decimal_places=2,default=0)

    create_time = models.DateField(verbose_name="入职时间")

    depart = models.ForeignKey(to="Department",to_field="id",null=True,blank=True,on_delete=models.SET_NULL)
    gender_choices = (
        (1,"male"),
        (2,"female")
    )
    gender = models.SmallIntegerField(choices = gender_choices)

class PrettyNum(models.Model):
    mobile = models.CharField(verbose_name="手机号",max_length=11)
    price = models.IntegerField(verbose_name="价格",default=0)
    level_choices = (
        (1,"1级"),
        (2,"2级"),
        (3,"3级"),
        (4,"4级")
    )

    level = models.SmallIntegerField(choices=level_choices,default=1)
    status_choices = (
        (1,"占用"),
        (2,"未占用")
    )
    status= models.SmallIntegerField(verbose_name="状态",choices=status_choices,default=2)
