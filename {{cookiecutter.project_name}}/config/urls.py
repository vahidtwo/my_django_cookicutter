from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from config.settings.swagger import schema_view

urlpatterns = [
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0)),
    path("adm/", admin.site.urls),
    path("api/v1/", include(("apps.urls.api", "api"))),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
