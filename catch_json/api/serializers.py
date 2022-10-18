from django.core.validators import FileExtensionValidator
from rest_framework import serializers


class FileSerializer(serializers.Serializer):
    file = serializers.FileField(
        required=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=["xlsx"]
            ),
        ]
    )

    class Meta:
        fields = ['file']


class OneArticleSerializer(serializers.Serializer):
    article = serializers.IntegerField(required=True)

    class Meta:
        fields = ['article']
