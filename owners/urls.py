from django.urls import path
from .views import *

urlpatterns = [
   path("", Ownersregister.as_view()),
   path("/dog", Dogsregister.as_view())
]
 