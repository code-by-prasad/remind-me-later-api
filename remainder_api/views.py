from http.client import responses

from django.core.serializers import serialize
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.status import HTTP_201_CREATED

from .models import Remainder
from .serializer import RemainderSerializer

@api_view(['GET'])
def get_data(request):
    remainders = Remainder.objects.all()
    serializer = RemainderSerializer(remainders, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def post_data(request):
    serializer = RemainderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

