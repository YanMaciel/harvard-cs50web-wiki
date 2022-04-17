from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>/", views.wiki_detail_view, name="wiki_detail"),
    path("search/", views.search, name="search"),
    path("random/", views.handle_random, name="random"),
    path("create-new-page/", views.create_new_page, name="create_new_page")
]
