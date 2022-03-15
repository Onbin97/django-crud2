from django.urls import path
from m2m.views import *

urlpatterns = [
    path("", Actorview.as_view()),
    path("/movie", MovieView.as_view()),
    path("/actormovie", Actormovieview.as_view())
   
]
 