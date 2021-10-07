from django.forms import ModelForm

from profileapp.models import Profile


class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        fields= ['play1_title','play1_rate','play2_title','play2_rate','play3_title','play3_rate']
