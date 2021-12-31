from authentication.models import User
from celery import shared_task

from django.core.mail import send_mail

from blog.settings import EMAIL_HOST_USER


@shared_task
def send_email_notice(users_id):
    users = User.objects.filter(id__in=users_id)
    send_mail('New post added!',
              'user add new post',
              EMAIL_HOST_USER,
              users)
    return None