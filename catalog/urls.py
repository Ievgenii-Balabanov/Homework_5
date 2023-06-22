from catalog import views

from django.urls import path


app_name = "catalog"
urlpatterns = [
    path("", views.index, name="index"),
    path("triangle/", views.get_cathetus, name="triangle"),
]
