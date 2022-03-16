from django.urls import path, include

urlpatterns = [
   path("owners", include("owners.urls")),
   path("m2m", include("m2m.urls")),
   path("books", include("books.urls")),
]
