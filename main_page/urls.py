from django.conf.urls import url

from . import views

app_name = 'main_page'

urlpatterns = [
    url(r'^contact/$', views.contact, name='contact'),

]
