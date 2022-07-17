from django.db import models
from django.forms import CharField, EmailField, PasswordInput
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


# Create your models here.

class ForumUser(User):
    login = CharField()
    password = PasswordInput()
    email = EmailField()

class BoardNotice(models.Model):

    CAT_CHOICES = [
        ('TK', 'Tank'),
        ('HP', 'Healer'),
        ('DD', 'Damage Dealer'),
        ('MC', 'Merchant'),
        ('GM', 'Guild Master'),
        ('QG', 'Quest Giver'),
        ('SM', 'Smith'),
        ('LT', 'Leatherman'),
        ('PM', 'Potion Maker'),
        ('MM', 'Master Mage'),
    ]
    
    author = models.ForeignKey(ForumUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=60 ,on_delete=models.CASCADE)
    text = RichTextField(on_delete=models.CASCADE)
    category = models.CharField(
        max_length=2,
        choices=CAT_CHOICES,
        default='QG',
        )

    def __str__(self):
        return f'{self.title} by {self.author}'