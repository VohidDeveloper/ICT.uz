from django.db import models

OPTION_CHOICES = (
    ('a', 'a'),
    ('b', 'b'),
    ('c', 'c'),
    ('d', 'd'),
)
class Quiz(models.Model):
    title = models.TextField()
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255, choices=OPTION_CHOICES)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Savollar bazasi"
