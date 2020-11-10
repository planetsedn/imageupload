from rest_framework import serializers
from imagelabel.models import ImageUpload


class ImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageUpload
        fields = ['photo', 'labels']