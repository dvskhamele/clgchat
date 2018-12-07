from django.conf.urls import url, include
from django.contrib import admin
from example_app.views import *


urlpatterns = [
    url(r'^chatterbot/', include('chatterbot.ext.django_chatterbot.urls', namespace='chatterbot')),
    url(r'^clear_all/$', ClearAll.as_view(), name='clear_all'),
    url(r'^$', ChatterBotAppView.as_view(), name='main'),
    url(r'^aaaaaa/$', TrainBotApiView.as_view(), name='aaaaaa'),
    url(r'^admin/', admin.site.urls, name='admin'),

]

#dvskha@gmail.com
#eightin8
#Eightin@8