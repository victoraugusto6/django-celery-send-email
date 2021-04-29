from django.http import HttpResponse
from .tasks import send_email_task


# Rodar Celery:
# celery -A django_email_celery worker -l info


def index(request):
    send_email_task.delay()
    return HttpResponse('<h1>E-MAIL FOI ENVIADO USANDO CELERY!</h1>')
