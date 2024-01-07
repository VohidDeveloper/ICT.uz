from django.db import models

# Create your models here.
class VideoCategory(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
        verbose_name_plural = "Video kategoriyalari"

class Video(models.Model):
    category = models.ForeignKey(VideoCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    video_id = models.CharField(max_length=255)
    rating = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
        verbose_name_plural = "Videolar"

class Maruza(models.Model):
    title = models.CharField(max_length=255)
    fan = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    maruza_fayl = models.FileField(upload_to='maruzalar')
    yuklashlar_soni = models.BigIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
        verbose_name_plural = "Ma'ruzalar"

class Slayd(models.Model):
    image = models.ImageField(upload_to='slaydlar')
    title = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    slayd_fayl = models.FileField(upload_to='slaydlar')
    yuklashlar_soni = models.BigIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
        verbose_name_plural = "Slaydlar"

class Amaliy(models.Model):
    title = models.CharField(max_length=255)
    fan = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    amaliy_fayl = models.FileField(upload_to='amaliylar')
    yuklashlar_soni = models.BigIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
        verbose_name_plural = "Amaliy mashg'ulotlar"

class Testlar(models.Model):
    title = models.CharField(max_length=255)
    fan = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    test_fayl = models.FileField(upload_to='testlar')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
        verbose_name_plural = "testlar"