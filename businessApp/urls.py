from django.urls import path
from . import views

app_name = 'businessApp'
urlpatterns = [
    path('', views.form, name='form'),
    path('table/', views.table, name='table'),
]