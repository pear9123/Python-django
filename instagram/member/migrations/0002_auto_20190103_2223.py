# Generated by Django 2.1.4 on 2019-01-03 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('m', '남성'), ('f', '여성'), ('o', '기타')], default='o', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='img_profile',
            field=models.ImageField(blank=True, upload_to='user'),
        ),
    ]