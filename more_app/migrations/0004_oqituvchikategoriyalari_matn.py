# Generated by Django 4.2.7 on 2023-12-22 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('more_app', '0003_oqituvchikategoriyalari_orqa_fon'),
    ]

    operations = [
        migrations.AddField(
            model_name='oqituvchikategoriyalari',
            name='matn',
            field=models.CharField(blank=True, max_length=455, null=True),
        ),
    ]
