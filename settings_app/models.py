from django.db import models

class OneHeader(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255, default="#")
    is_submenu = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "1-Darajali menyular"
        ordering = ['id']

class TwoHeader(models.Model):
    one_header = models.ForeignKey(OneHeader, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255, default="#")
    is_submenu = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "2-Darajali menyular"
        ordering = ['id']

class LogoSettings(models.Model):
    title = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='logos')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Logo sozlamalari"
        ordering = ['id']

class RightButtonSettings(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "O'ng tugmacha sozlamalari"
        ordering = ['id']

class FooterSettings(models.Model):
    title = models.CharField(max_length=455)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Footer sozlamalari"
        ordering = ['id']

class SocialSettings(models.Model):
    title = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Ijtimoiy tarmoqlar"
        ordering = ['id']

class PhoneEmailSettings(models.Model):
    phone1 = models.CharField(max_length=255)
    phone2 = models.CharField(max_length=255)

    email1 = models.CharField(max_length=255)
    email2 = models.CharField(max_length=255)

    def __str__(self):
        return self.phone1

    class Meta:
        verbose_name_plural = "Telefon va email sozlamalari"
        ordering = ['id']

class SeoSettings(models.Model):
    title = models.CharField(max_length=255)
    keywords = models.TextField()
    description = models.TextField()
    author = models.CharField(max_length=255)
    favicon = models.FileField(upload_to='favicons')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Seo sozlamalari"
        ordering = ['id']

class TelegramBotSettings(models.Model):
    title = models.CharField(max_length=255)
    token = models.CharField(max_length=455)
    user_id = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Telegram bot sozlamalari"
        ordering = ['id']
