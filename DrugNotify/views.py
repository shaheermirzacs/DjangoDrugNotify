# views.py

from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer, TestSerializer
from .models import User, Test
import os

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ['identifier']

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    search_fields = ['=user__identifier']
    filter_backends = (filters.SearchFilter,)

@api_view(['POST'])
def check(request):
    phone = request.data['phone']
    name = request.data['last_name']
    ivr_code = request.data['ivr_code']
    token = request.data['token']
    id = request.data['identifier']

    print(request.data['token'])
    cmd = './notify.exe {0} {1} {2} {3} {4}'.format(phone, name, ivr_code, token, id)
    #cmd = 'ls'
    os.system(cmd)
    return Response('howdy')
