# pylint: disable=unused-wildcard-import, wildcard-import
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from sss.app.viewsets import *
from sss.app.viewsets.base.base_viewset import ModelViewSet

__all__ = ["urlpatterns"]

router = routers.SimpleRouter(trailing_slash=False)
for route in ModelViewSet.__subclasses__():
    router.register(route.pathname, route, basename=route.pathname)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include((router.urls, "app"), namespace="api")),
]
