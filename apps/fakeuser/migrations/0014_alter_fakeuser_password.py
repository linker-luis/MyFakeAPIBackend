# Generated by Django 3.2.6 on 2021-09-18 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fakeuser', '0013_alter_fakeuser_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fakeuser',
            name='password',
            field=models.CharField(default='2a328092', max_length=8),
        ),
    ]
