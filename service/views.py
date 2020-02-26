from rest_framework import viewsets

from service.models import FileMetadata
from service.serializers import FileMetadataSerializer


class FileMetadataViewSet(viewsets.ModelViewSet):
    queryset = FileMetadata.objects.all()
    serializer_class = FileMetadataSerializer
    http_method_names = ["get", "post", "patch", "delete", "head", "options"]
