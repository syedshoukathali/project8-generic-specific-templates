from django.urls import path
from app1.views import *
app_name='something1'


urlpatterns=[
    path('string_1/',string_1,name='string_1'),
    path('string_2/',string_2,name='string_2'),
]