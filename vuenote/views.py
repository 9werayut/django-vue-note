from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from vuenote.serializers import NoteSerializers
from .models import Note

#Note viewset
#Create, edit ordisplay our notes via API

class NoteViewSet(viewsets.ModelViewSet):
    # check permission
    permission_classes = (
        IsAuthenticated,
    )
    queryset = Note.objects.all()
    serializer_class = NoteSerializers
    lookup_field = 'id'