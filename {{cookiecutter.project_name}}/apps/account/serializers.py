from django.http import Http404
from rest_framework import serializers

from apps.account.models import User


class EmailLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(min_length=8)


class ForgetPasswordRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate(self, attrs):
        user = User.objects.filter(email=attrs.get("email")).first()
        if user is None:
            raise Http404("user not found")
        return attrs
