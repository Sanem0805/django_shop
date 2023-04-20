from django.core.mail import send_mail
from celery import shared_task


@shared_task
def send_confirmation_mail(username, address, pk, email):
    message = f"""
    Здравствуйте, {username}!
    Подтвердите заказ на адресс {address}!
    http:/localhost:8000/oder/{pk}/confirm/
    Если это были не вы игнорируйте это сообщение
    """
    send_mail(
        subject='Подтвердите заказ',
        message=message,
        from_email='test@test.com',
        recipient_list=[email],
        fail_silently=False

    )