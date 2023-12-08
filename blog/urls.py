from django.urls import path
from .views import index, contact, about, post

urlpatterns = [
    path("", index, name="Index"),
    path("post/", post, name="Post"),
    path("about/", about, name="About"),
    path("contact/", contact, name="Contact"),
]
