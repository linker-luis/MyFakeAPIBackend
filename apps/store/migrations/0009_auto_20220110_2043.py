# Generated by Django 3.2.6 on 2022-01-11 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_rename_decription_category_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='imgURL',
            field=models.URLField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='images',
            name='img',
            field=models.ImageField(null=True, upload_to='store/'),
        ),
    ]
