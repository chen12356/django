
from rest_framework import serializers

from FbvDrfApp.models import BathCenter


class BathCenterSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    price = serializers.IntegerField()


    def create(self, validated_data):

        return BathCenter.objects.create(**validated_data)


    def update(self, instance, validated_data):

        instance.id = validated_data.get('id',instance.id)
        instance.name = validated_data.get('name',instance.name)
        instance.price = validated_data.get('price',instance.price)

        instance.save()
        return instance





