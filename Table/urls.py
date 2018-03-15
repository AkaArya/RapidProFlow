from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('choice', views.choice, name='choice'),
    url(r'^(?P<flow_id>[0-9]\d+)$',views.analyse, name='analyse'),
    path('test', views.test, name='test'),
    path('get-form-questions', views.getFormParam, name='getFormParam'),
    path('get-form-questions-choice', views.getFormParamChoice, name='getFormParamChoice')

]
