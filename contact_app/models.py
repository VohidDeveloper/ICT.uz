from django.db import models

# Create your models here.
class AboutMe(models.Model):
    image = models.ImageField(upload_to='about-me')
    title = models.CharField(max_length=255)

    manzil_title = models.CharField(max_length=255)
    manzil_body = models.CharField(max_length=255)

    phone_title = models.CharField(max_length=255)
    phone_body = models.CharField(max_length=255)

    email_title = models.CharField(max_length=255)
    email_body = models.CharField(max_length=255)

    map = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Men haqimda"
        ordering = ['id']

class Message(models.Model):
    name = models.CharField(max_length=455)
    tg_username = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.message

    class Meta:
        verbose_name_plural = "Tizimga kelgan xabarlar"
        ordering = ['-id']