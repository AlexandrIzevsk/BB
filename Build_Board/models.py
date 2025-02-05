from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='users')


class Advert(models.Model):
    tanks = 'Tk'
    hills = 'Hl'
    dd = 'DD'
    merchants = 'Mr'
    gild_masters = 'Gm'
    kvest_givers = 'Kg'
    blacksmiths = 'Bm'
    tanners = 'Tn'
    potion_makers = 'Pm'
    spellmasters = 'Sm'

    CHOICES = [
        (tanks, 'Танки'),
        (hills, 'Хиллы'),
        (dd, 'ДД'),
        (merchants, 'Торговцы'),
        (gild_masters, 'Гилдмастера'),
        (kvest_givers, 'Квестгиверы'),
        (blacksmiths, 'Кузнецы'),
        (tanners, 'Кожевники'),
        (potion_makers, 'Зельевары'),
        (spellmasters, 'Мастера заклинаний')
    ]

    author = models.ForeignKey(Customer, on_delete=models.CASCADE)
    choice = models.CharField(max_length=2, choices=CHOICES, default=tanks)
    time_in = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=128)
    content = HTMLField()

    def __str__(self):
        return f'{self.title} - {self.preview()}'

    def preview(self):
        return self.content[0:123] + '...'

    def get_absolute_url(self):
            return reverse('advert_detail', args=[str(self.id)])


class Feedback(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    advert = models.ForeignKey(Advert, on_delete=models.CASCADE)
    time_in = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    accept = models.BooleanField(default=False)
