# Generated by Django 3.1.2 on 2020-10-04 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='others',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
