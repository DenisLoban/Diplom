from abc import ABC

from rest_framework.serializers import ModelSerializer, Serializer
from shop.models import Category
from rest_framework.fields import CharField, IntegerField


class CategorySerializer(ModelSerializer):
    class Meta:
        slug = CharField(required=False)
        model = Category
        fields = ('id', 'name')


class CalculatorSerializer(Serializer):

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    height = IntegerField(min_value=1)
    width = IntegerField(min_value=1)