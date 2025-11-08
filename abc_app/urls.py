from django.urls import path
from . import views

app_name = 'abc_app'
urlpatterns = [
    path('', views.abc_model_form, name='abc_model_form'),
    path('abc_result/', views.abc_result, name='abc_result'),
    path('table/', views.table, name='table'),
]