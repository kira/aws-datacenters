from django.conf.urls import url
from django.contrib import admin

from aws_datacenters.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', MediaServerMap.as_view()),
]
