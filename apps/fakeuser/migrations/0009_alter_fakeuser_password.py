# Generated by Django 3.2.6 on 2021-09-01 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fakeuser', '0008_alter_fakeuser_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fakeuser',
            name='password',
            field=models.CharField(default='934bc3e8', max_length=8),
        ),
    ]
