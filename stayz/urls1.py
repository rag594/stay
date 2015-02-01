from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from stayz import views1

urlpatterns = patterns('',

    url(r'^$',views1.shre,name='shre'),

)
    

