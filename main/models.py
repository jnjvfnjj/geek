from django.db import models

# Create your models here.
class Index(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    description = models.TextField(
        verbose_name="описание"
    )
    logo = models.ImageField(
        upload_to='logo_image/',
        verbose_name="логотип",
    )
