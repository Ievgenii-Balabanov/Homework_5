from catalog import views

from django.urls import include, path


app_name = "catalog"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("person/<int:pk>", views.PersonDetailView.as_view(), name="detail"),
    path("create/", views.create_person, name="create_person"),
    path("update/<int:pk>", views.update_person, name="update_person"),
    path("delete/<int:pk>", views.delete_person, name="delete_person"),
    # path("triangle/", views.get_cathetus, name="triangle"),
]
