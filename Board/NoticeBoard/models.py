from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


# Create your models here.

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

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    text = RichTextField()
    creation = models.DateTimeField(auto_now_add=True)
    category = models.CharField(
        max_length=2,
        choices=CAT_CHOICES,
        default='QG',
        )
    
    def __str__(self):
        return f'{self.title} by {self.user}, {self.category}.'

class Response(models.Model):
    response_user = models.ForeignKey(User, on_delete=models.CASCADE)
    response_to = models.ForeignKey(BoardNotice, on_delete=models.CASCADE)
    creation = models.DateTimeField(auto_now_add=True)
    text = RichTextField()
    accepted = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-creation']
    
    def __str__(self):
        return f'{self.response_user}. {self.creation}: {self.text}'