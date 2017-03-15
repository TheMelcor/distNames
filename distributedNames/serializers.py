from rest_framework import serializers
from distributedNames.models import Name, Node


class NameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Name
        fields = ('id', 'name')


class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = ('ip', 'isAuth')
