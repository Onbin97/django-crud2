from django.urls import path
from books.views import *

urlpatterns = [
    path("", Bookview.as_view()),
    path("/authors", Authorview.as_view())    
]
 