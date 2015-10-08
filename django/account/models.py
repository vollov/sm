from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    phone = models.CharField(max_length=64, blank=True, null=True)
    id = models.CharField(max_length=64, primary_key=True, verbose_name=u"Activation key",
                 default=uuid.uuid4)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username