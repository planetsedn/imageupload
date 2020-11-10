from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
from rest_framework import viewsets
from imagelabel.myserializer import ImageUploadSerializer
from imagelabel.models import ImageUpload




class ImageUploadViewSet(viewsets.ModelViewSet):

  queryset = ImageUpload.objects.all()
  serializer_class = ImageUploadSerializer