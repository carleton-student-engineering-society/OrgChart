from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("search/<str:pattern>/", views.search_pattern, name="search_pattern"),
    path("view", views.view, name="view"),
    path("view/<str:org>", views.view_org, name="view_org"),
    path("add/<str:org/", views.add, name="add"),
    path("create_org", views.create_org, name="create_org"),

]
