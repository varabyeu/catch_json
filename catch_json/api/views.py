from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import FileSerializer
from .async_parser import distribute_tasks
from .utils import get_articles


class FileUploadView(APIView):

    def post(self, request):
        serializer = FileSerializer(data=request.FILES)
        serializer.is_valid(raise_exception=True)
        product_articles, invalid_articles = get_articles(request.FILES.get('file'))
        if len(product_articles) == 0:
            return Response(
                {
                    'Error': 'There is not any valid articles',
                },
                status=status.HTTP_404_NOT_FOUND
            )
        gathered_data = distribute_tasks(product_articles)
        return Response({'data': gathered_data}, status=status.HTTP_200_OK)


class ArticleView(APIView):
    pass
