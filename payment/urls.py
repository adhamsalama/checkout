from django.urls import path

from . import views

app_name = "payment"

urlpatterns = [
    path("", views.index, name="index"),
    path("add_payment", views.add, name="add"),
    path("delete_payment", views.delete, name="delete")
]