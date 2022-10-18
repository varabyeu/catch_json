from django.urls import path
from .views import FileUploadView, ArticleView

urlpatterns = [
    path('from_file/', FileUploadView.as_view()),
    path('article/', ArticleView.as_view())
]