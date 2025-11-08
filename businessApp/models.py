from django.db import models



class businessApp(models.Model):
   
    r_name= models.CharField(
        verbose_name="Название ресурса",
        default="отсутствует",
        max_length=255,
    )

    r_amount=models.IntegerField(
        verbose_name="Количество ресурса", default=0,
        )

    r_price=models.FloatField(
        verbose_name="Цена ресурса", default=0,
        )
    
    s_name= models.CharField(
        verbose_name="Название товара",
        default="отсутствует",
        max_length=255,
    )

    s_amount=models.IntegerField(
        verbose_name="Количество товара", default=0,
        )

    s_price=models.FloatField(
        verbose_name="Цена товара", default=0,
        )
    current_date = models.DateTimeField(
        verbose_name="Дата изменения(save)", auto_now=True
    )


    def __str__(self):
        # return self.task
        # return '%s %s' % (self.task, self.current_date)
        return f"self.id:{self.id}; self.r_name:{self.r_name}; self.s_name:{self.s_name}"

    class Meta:
        verbose_name = "Таблица"
        verbose_name_plural = "Таблицы"
        ordering = ("id", )
 

# current_date = models.DateTimeField("ДатаВремя", default=datetime.datetime.now())
# current_date = models.DateTimeField("ДатаВремя", auto_now_add=True)

# python manage.py makemigrations
# python manage.py migrate

# admin.py
# from django.contrib import admin
# # Register your models here.
# from .models import Abc
# admin.site.register(Abc)


# forms.py
# from django.forms import ModelForm
# from .models import Abc
#
# class CreateAbcForm(ModelForm):
#     class Meta:
#         model = Abc
#         fields = ['task', 'a' ,'b' ,'c', 'c_calc']