from django import forms
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.contrib.auth.models import User

from qna_profile.models import UserProfile

class UserProfileForm(forms.ModelForm):
    email = forms.EmailField(required=False)

    def __init__(self, *args, **kwargs):
        instance = kwargs.pop('instance', None)
        initial = kwargs.pop('initial', {})
        if instance:
            initial['email'] = instance.user.email
        super(UserProfileForm, self).__init__(
            initial=initial, instance=instance, *args, **kwargs
        )


    class Meta:
        model = UserProfile
        exclude = ('user', )

    def clean_email(self):
        """For security reason one unique email in database"""
        if self.instance.user.email != self.cleaned_data['email']:
            #todo dry it, there is a similar thing in openidauth
            if getattr(settings, 'EMAIL_UNIQUE', True) == True:
                if 'email' in self.cleaned_data:
                    try:
                        user = User.objects.get(email = self.cleaned_data['email'])
                    except User.DoesNotExist:
                        return self.cleaned_data['email']
                    except User.MultipleObjectsReturned:
                        pass
                    raise forms.ValidationError(_('this email has already been registered, please use another one'))
        return self.cleaned_data['email']
    
    def save(self, user=None):
        profile = super(UserProfileForm, self).save()

        if self.cleaned_data['email']:
            profile.user.email = self.cleaned_data['email']
            profile.user.save()
        
        return profile
    