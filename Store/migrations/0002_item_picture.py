# Generated by Django 4.0.3 on 2022-03-27 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='picture',
            field=models.CharField(default='', max_length=20, verbose_name='Picture'),
        ),
    ]
