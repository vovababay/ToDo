from django.contrib.auth.models import User, AnonymousUser

from boards.serializers import NoteSerializer, NotedetailSerializer, UserSerializer
from boards.models import Note
from rest_framework import generics
from rest_framework import permissions
from boards.permissions import IsOwnerOrReadOnly


class NoteList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    serializer_class = NoteSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Note.objects.filter(author=self.request.user)

        else:
            return None

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    queryset = Note.objects.all()
    serializer_class = NotedetailSerializer


class CreateUser(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
