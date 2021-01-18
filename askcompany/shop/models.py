from django.conf import settings
from django.db import models
from askcompany.utils import uuid_upload_to
from django.urls import reverse

class Item(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    photo = models.ImageField(blank=True, upload_to=uuid_upload_to)
    is_publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'<{self.pk}> {self.name}'
    
    def get_absolute_url(self):
        return reverse('shop:item_detail', kwargs={'pk':self.pk})

    class Meta:
        ordering = ['id']

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
