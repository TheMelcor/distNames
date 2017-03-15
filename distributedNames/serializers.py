from rest_framework import serializers
from distributedNames.models import Name, Node


class NameSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=False, max_length=50)

    def create(self, validated_data):
        return Name.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class NodeSerializer(serializers.Serializer):
    ip = serializers.CharField(required=True, allow_blank=False, max_length=15)
    isAuth = serializers.BooleanField()

    def create(self, validated_data):
        return Node.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.ip = validated_data.get('ip', instance.ip)
        instance.isAuth = validated_data.get('isAuth', instance.isAuth)
        instance.save()
        return instance
