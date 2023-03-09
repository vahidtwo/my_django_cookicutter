from rest_framework.serializers import ModelSerializer as DRFModelSerializer

from .abstract_base_serializer import AbstractBaseSerializer


class ModelSerializer(AbstractBaseSerializer, DRFModelSerializer):
    pass
