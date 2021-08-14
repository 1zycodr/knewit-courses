# Generated by Django 3.2.6 on 2021-08-13 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_course_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=8, null=True, verbose_name='Цена'),
        ),
    ]