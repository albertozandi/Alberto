from django.contrib.auth.models import User, Group
from zuaya.models import Cuisine
from rest_framework import viewsets
from zuaya.serializers import UserSerializer, GroupSerializer, CusisineSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class CuisineViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Cuisine.objects.all()
    serializer_class = CusisineSerializer