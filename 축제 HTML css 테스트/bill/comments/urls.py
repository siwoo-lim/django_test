from django.urls import path
from .views import *

urlpatterns = [
    path('comment/billboard/', comments_load, name='billboard'),
    path('comment/', get_comment, name="writecomment"),
]
