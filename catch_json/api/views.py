from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import FileSerializer, OneArticleSerializer
from .async_parser import distribute_tasks
from .utils import get_articles


class FileUploadView(APIView):
    """View to upload xlsx file

    Use only post method to attach a file.
    This view func manages a parsing process
    """
    def post(self, request):
        serializer = FileSerializer(data=request.FILES)
        serializer.is_valid(raise_exception=True)
        product_articles, invalid_articles = get_articles(
            request.FILES.get('file')
        )
        if len(product_articles) == 0:
            return Response(
                {
                    'Error': 'There is not any valid articles',
                },
                status=status.HTTP_404_NOT_FOUND
            )
        gathered_data = distribute_tasks(product_articles)
        return Response(
            gathered_data if len(gathered_data) > 1 else gathered_data[0],
            status=status.HTTP_200_OK
        )


class ArticleView(APIView):
    """View to work with alone article

    Use only post to send article to parse data
    """
    def post(self, request):
        serializer = OneArticleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        gathered_data = distribute_tasks([request.data.get('article'), ])[0]
        return Response(
            gathered_data, status.HTTP_200_OK
        )
