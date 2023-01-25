from django.urls import path
from .import views
# from board.views import list


urlpatterns = [
    path("index", views.index, name="board_index"),
    path("detail/<int:pk>/", views.detail, name="board_detail"),
    path("write", views.update, name="board_write"),
    path("delete/<int:pk>/", views.remove, name="board_remove"),
    path("edit/<int:pk>/", views.edit, name="board_edit")

]
