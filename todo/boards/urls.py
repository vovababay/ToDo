
from django.urls import path, include
from boards.views import *

urlpatterns = [
    path('note/', NoteList.as_view()),
    path('note/<int:pk>', NoteDetail.as_view()),
    path('user/', CreateUser.as_view()),
]
