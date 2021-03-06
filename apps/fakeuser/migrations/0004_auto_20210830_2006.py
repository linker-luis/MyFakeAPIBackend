# Generated by Django 3.2.6 on 2021-08-31 01:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fakeuser', '0003_auto_20210830_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='fakeuser.fakeuser'),
        ),
        migrations.AlterField(
            model_name='faketoken',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='token', to='fakeuser.fakeuser'),
        ),
        migrations.AlterField(
            model_name='fakeuser',
            name='password',
            field=models.CharField(default='e0a94460', max_length=8),
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='personal_information', to='fakeuser.fakeuser'),
        ),
    ]
