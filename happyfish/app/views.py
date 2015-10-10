from django.shortcuts import render
from app.models import Aquarium
from app.serializers import AquariumSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['POST'])
def upload_data(request):
    print request.data
    temperature = request.data['temperature']
    ph = request.data['ph']
    data = Aquarium.objects.create(temperature=temperature, ph=ph)
    serializer = AquariumSerializer(data)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_data(request):
    data = Aquarium.objects.latest('updated_time')
    serializer = AquariumSerializer(data)
    return Response(serializer.data)
