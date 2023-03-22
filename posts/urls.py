from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostList.as_view(), name="post-list"),
    path("<int:pk>/", views.PostDetail.as_view(), name="post-detail"),
    path("new/", views.PostCreate.as_view(), name="post-create"),
    path("<int:pk>/edit/", views.PostEdit.as_view(), name="post-edit"),
    path("<int:pk>/delete/", views.PostDelete.as_view(), name="post-delete"),
]