from django.urls import path

from . import views

app_name = "wishlist"

urlpatterns = [
    path("", views.index, name="index"),
    path("get_wishlist_form", views.get_form, name="get_wishlist_form"),
    path("add", views.add_wishlist, name="add_wishlist"),
    path("delete", views.delete_wishlist, name="delete_wishlist")
]