# Generated by Django 3.2.6 on 2022-03-28 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fakeuser', '0024_alter_fakeuser_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='fakeuser.personalinformation'),
        ),
        migrations.AlterField(
            model_name='fakeuser',
            name='password',
            field=models.CharField(default='3a7c7ad1', max_length=8),
        ),
    ]
