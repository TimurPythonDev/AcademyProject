# Generated by Django 4.0.3 on 2022-03-19 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_sendregistr_is_read'),
    ]

    operations = [
        migrations.AddField(
            model_name='sendregistr',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
