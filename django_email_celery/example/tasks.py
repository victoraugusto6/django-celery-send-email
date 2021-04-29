from celery import shared_task
from time import sleep
from django.core.mail import send_mail


@shared_task
def sleepy(duration):
    sleep(duration)
    return None


@shared_task
def send_email_task():
    sleep(10)
    send_mail('Celery funcionou!',
              'E-mail enviado via Celery.',
              'victor.augusto60@gmail.com',
              ['yabico1303@sumwan.com'])
    return None
