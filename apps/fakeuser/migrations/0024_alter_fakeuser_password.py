# Generated by Django 3.2.6 on 2022-01-20 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fakeuser', '0023_alter_fakeuser_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fakeuser',
            name='password',
            field=models.CharField(default='40978b06', max_length=8),
        ),
    ]
