from rest_framework import serializers

from service.models import FileMetadata


class FileMetadataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FileMetadata
        fields = [
            "url",
            "id",
            "name",
            "description",
            "type",
            "size",
            "location",
            "created",
            "updated",
        ]
        read_only_fields = ["url", "id", "created"]
