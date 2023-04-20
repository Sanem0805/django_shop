from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from celery import shared_task


User = get_user_model()


@shared_task
def send_periodic_mail():
    user_emails = User.objects.all().values('email')
    send_mail(
        subject="Hello!",
        message='Good morning',
        from_email='test@test.com',
        recipient_list=[user.email for user in user_emails],
        fail_silently=False

    )