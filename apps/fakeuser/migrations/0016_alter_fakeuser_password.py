# Generated by Django 3.2.6 on 2021-11-04 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fakeuser', '0015_alter_fakeuser_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fakeuser',
            name='password',
            field=models.CharField(default='2271d046', max_length=8),
        ),
    ]
