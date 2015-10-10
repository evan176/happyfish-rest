from django.shortcuts import render
from app.models import Aquarium
from app.serializers import AquariumSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

# Create your views here.

@api_view(['POST'])
def upload_data(request):
    print request.data
    temperature = request.data['temperature']
    ph = request.data['ph']
    aquarium = Aquarium.objects.create(temperature=temperature,
                                       ph=ph)
    serializer = AquariumSerializer(aquarium)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
