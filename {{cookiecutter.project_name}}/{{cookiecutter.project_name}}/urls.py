"""{{cookiecutter.project_name}} URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from {{cookiecutter.project_name}}.swagger import schema_view

urlpatterns = [
    path("adm/", admin.site.urls),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0)),
    path("", include("apps.urls.web")),
    path("api/v1/", include("apps.urls.api")),
    path("i18n/", include("django.conf.urls.i18n")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if os.environ.get("DJANGO_SETTINGS_MODULE") == "{{cookiecutter.project_name}}.local":
    urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")))
handler404 = "apps.web.views.notfound_view"
