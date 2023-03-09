from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


SWAGGER_SETTINGS = {
    "SECURITY_DEFINITIONS": {
        "Basic": {"type": "basic"},
        "Token": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": 'Add word "Token " before your token value',
        },
    }
}

schema_view = get_schema_view(
    openapi.Info(
        title="Bernet API",
        default_version="v1",
        description="bernet apis",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,  # TODO: change permission to superuser only
    permission_classes=(permissions.AllowAny,),
)
