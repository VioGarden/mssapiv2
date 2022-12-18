from rest_framework import serializers
from .models import Songs
from api.serializers import UserPublicSerializer
from rest_framework.reverse import reverse


class SongsSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user', read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='songs-detail',
        lookup_field='pk'
    )
    edit_url = serializers.SerializerMethodField(read_only=True)
    delete_url = serializers.SerializerMethodField(read_only=True)

    urls = {
        'url': url,
        'edit_url': edit_url,
        'delete_url': delete_url,
    }
    class Meta:
        model = Songs
        fields = [
            'owner',
            'url',
            'edit_url',
            'delete_url',
            'title',
            'titleRom',
            'song', 
            'artist', 
            'opedin',
            'video',
            'audio',
        ]

    def create(self, validated_data):
        return Songs.objects.create(**validated_data)
    
    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("songs-update", kwargs={"pk": obj.pk}, request=request)

    def get_delete_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("songs-destroy", kwargs={"pk": obj.pk}, request=request)