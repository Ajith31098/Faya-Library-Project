# Generated by Django 4.1 on 2023-02-21 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approvalforuser',
            name='approval',
            field=models.BooleanField(default=False),
        ),
    ]
