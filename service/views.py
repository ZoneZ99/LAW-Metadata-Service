from django.utils.decorators import method_decorator
from rest_framework import viewsets

from service.decorators import oauth_check
from service.models import FileMetadata
from service.serializers import FileMetadataSerializer


@method_decorator(oauth_check, name="dispatch")
class FileMetadataViewSet(viewsets.ModelViewSet):
    queryset = FileMetadata.objects.all()
    serializer_class = FileMetadataSerializer
    http_method_names = ["get", "post", "patch", "delete", "head", "options"]
