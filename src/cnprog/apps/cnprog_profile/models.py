from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="cnprog_profile")
    real_name = models.fields.CharField(_('real name'), max_length=100, blank=True)
    website = models.fields.URLField(_('website'), max_length=200, blank=True)
    location = models.fields.CharField(_('location'), max_length=100, blank=True)
    date_of_birth = models.fields.DateField(_('date of birth'), null=True, blank=True)
    about = models.fields.TextField(_('about'), blank=True)
    is_public = models.BooleanField(default=True, editable=False)
    
    @models.permalink
    def get_absolute_url(self):
        return ('profiles_profile_detail',
                (), { 'username': self.user.username })

def create_profile(instance, created, **kwargs):
    if created:
        UserProfile(user=instance).save()
post_save.connect(create_profile, sender=User)
