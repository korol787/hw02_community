# Generated by Django 2.2 on 2020-07-22 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20200722_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
