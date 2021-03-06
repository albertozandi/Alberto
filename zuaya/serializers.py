from django.contrib.auth.models import User, Group
from zuaya.models import Cuisine
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class CusisineSerializer(serializers.HyperlinkedModelSerializer):
    """
    This is the cuisine serialiser that specifies which attributes are used in the REST API.
    """
    class Meta:
        model = Cuisine
        fields = ('name', 'description', 'price')