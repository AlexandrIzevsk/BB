from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import Feedback


@receiver(post_save, sender=Feedback)
def product_created(instance, **kwargs):
    emails = User.objects.filter(advert=instance.advert).values_list('email', flat=True)
    for email in emails:
        send_mail(
            subject='Отклик на объявление',
            message=f'Пользователь {instance.user.username} оставил отклик на объявление {instance.advert.title}',
            from_email=None,
            recipient_list=[email],
        )