from django.conf.urls import url

from . import views

app_name = 'main_page'

urlpatterns = [
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$', views.about, name='about'),
    url(r'^projects/$', views.projects, name='projects'),
    url(r'^resume.docx/$', views.resume, name='resume'),

]
