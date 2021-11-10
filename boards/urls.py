from django.urls import path

from .views import ListBoardsView, DetailBoardView, CommentsView, UpdateCommentsView


app_name = 'boards'
urlpatterns = [
    # path('', board_list),
    # path('<int:pk>/', board_detail),
    # path('<int:pk>/comments/', comments),
    # path('<int:pk>/comments/<int:comment_pk>', comments_update)

    path('', ListBoardsView.as_view()),
    path('<int:pk>/', DetailBoardView.as_view()),
    path('<int:pk>/comments/', CommentsView.as_view()),
    path('<int:pk>/comments/<int:comment_pk>', UpdateCommentsView.as_view()),
]