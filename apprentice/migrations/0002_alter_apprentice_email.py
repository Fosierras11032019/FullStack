# Generated by Django 4.1.2 on 2022-10-24 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apprentice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apprentice',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
    ]
