from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# so every user will always have a token associated to its account
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_account_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
