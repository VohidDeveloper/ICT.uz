from django.db import models

class OqituvchiKategoriyalari(models.Model):
    nomi = models.CharField(max_length=455)
    matn = models.CharField(max_length=455, null=True, blank=True)
    orqa_fon = models.ImageField(upload_to='backgrounds', null=True, blank=True)

    def __str__(self):
        return self.nomi

    class Meta:
        ordering = ['id']

class MeyoriyXujjatlar(models.Model):
    kategoriyasi = models.ForeignKey(OqituvchiKategoriyalari, on_delete=models.CASCADE)
    nomi = models.CharField(max_length=455)
    fayl = models.FileField(upload_to='meyoriy-xujjatlar')
    yuklashlar_soni = models.BigIntegerField(default=0)

    def __str__(self):
        return self.nomi

    class Meta:
        ordering = ['id']

