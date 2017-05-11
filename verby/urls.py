from django.conf.urls import url
from verby import views

urlpatterns = [
        url(r'^writer_signup/$', views.writer_signup, name="writer_signup"),

]
