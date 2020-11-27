from django.urls import path

from . import views

app_name = "checkout"

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_item", views.create_item, name="create_item"),
    path("profile", views.profile, name="profile"),
    path("edit_item/<int:item_id>", views.edit_item, name="edit_item"),
    path("delete_item", views.delete_item, name="delete_item"),
    path("update_balance", views.update_balance, name="update_balance"),
    path("search", views.search, name="search"),
    path("search/<str:q>", views.search_page, name="search_page"),
    path("categories/<str:name>", views.category, name="category"),
    path("change_password", views.change_password, name="change_password")
]