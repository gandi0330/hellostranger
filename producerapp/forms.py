from django.forms import ModelForm, forms

from producerapp.models import Play


class PlayCreationForm(ModelForm):

    class Meta:
        model = Play
        fields = ['title', 'genre','image','location','etc']
