from django.shortcuts import render
from django.contrib.auth.models import Group, User
from api.models import GeeksModel
from rest_framework import permissions, viewsets
from api.serializers import GroupSerializer, UserSerializer, GeeksSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class GeeksViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = GeeksModel.objects.all().order_by('title').filter(ready=True)
    serializer_class = GeeksSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]