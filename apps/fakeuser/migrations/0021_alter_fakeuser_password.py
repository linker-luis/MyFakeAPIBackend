# Generated by Django 3.2.6 on 2022-01-11 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fakeuser', '0020_alter_fakeuser_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fakeuser',
            name='password',
            field=models.CharField(default='fbe5e912', max_length=8),
        ),
    ]
