from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>/", views.wiki_detail_view, name="wiki_detail"),
    path("search/<str:searched_entry>/", views.search_entry_view, name="search")
]
