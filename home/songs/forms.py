from django import forms

from .models import Songs

class SongsForm(forms.ModelForm):
    class Meta:
        model = Songs
        fields = [
            'title',
            'titleRom',
            'song', 
            'artist', 
            'opedin',
            'video',
            'audio',
        ]