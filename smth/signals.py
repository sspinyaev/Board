from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import UserResponse
from django.contrib.auth.models import User


@receiver(pre_save, sender=User)
def my_handler(sender, instance, created, **kwargs):
    if instance.status is not True:
        return
    mail = instance.article.author.mail
    send_mail(
        'Subject_Here',
        'Here is the message',
        'example@YANDEX.ru',
        [mail],
        fail_silently = False,
    )
