from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import generics, mixins, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Songs
from .serializers import SongsSerializer

from api.mixins import StaffEditorPermissionMixin

class SongsDetailAPIView(generics.RetrieveAPIView):
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer

songs_detail_view = SongsDetailAPIView.as_view()

class SongsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer

    def perform_create(self, serializer):
        serializer.save()
songs_list_create_view = SongsListCreateAPIView.as_view()

class SongsUpdateAPIView(generics.UpdateAPIView):
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        serializer.save()

songs_update_view = SongsUpdateAPIView.as_view()

class SongsDestroyAPIView(generics.DestroyAPIView):
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

songs_destroy_view = SongsDestroyAPIView.as_view()