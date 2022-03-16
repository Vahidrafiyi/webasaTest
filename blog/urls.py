from django.urls import path, re_path
from .views import *

urlpatterns = [
    re_path(r'articles/(?P<pk>[0-9]*)', ShowArticle.as_view()),
    # path('add_article/', AddArticle.as_view()),
    path('comments/<int:pk>', CommentRelatedToArticle.as_view()),
    path('comments/<int:pk>/vote', VoteCreate.as_view()),
]
