# Generated by Django 2.1.4 on 2019-01-03 13:28

from django.db import migrations, models
import member.models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20190103_2223'),
        ('member', '0002_auto_20190103_2223'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', member.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='like_posts',
            field=models.ManyToManyField(blank=True, related_name='like_users', to='post.Post'),
        ),
    ]
