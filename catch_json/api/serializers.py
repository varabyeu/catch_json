from django.core.validators import FileExtensionValidator
from rest_framework import serializers


class FileSerializer(serializers.Serializer):
    """File Serializer

    To Serialize files with xlsx extension.
    """
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
    """One Article Serializer

    Serializes alone article
    """

    article = serializers.IntegerField(required=True)

    class Meta:
        fields = ['article']
