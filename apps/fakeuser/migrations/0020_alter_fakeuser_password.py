# Generated by Django 3.2.6 on 2022-01-11 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fakeuser', '0019_alter_fakeuser_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fakeuser',
            name='password',
            field=models.CharField(default='0b28680f', max_length=8),
        ),
    ]
