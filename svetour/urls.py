from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^andorra/$', views.andorra, name='andorra'),
    url(r'^shusskiapthl/$', views.shusskiapthl, name='shusskiapthl'),
]