from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="{{ cookiecutter.project_name}} API",
        default_version="v1",
        description="{{ cookiecutter.project_slug apis",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,  # TODO: change permission to superuser only
    permission_classes=(permissions.AllowAny,),
)
