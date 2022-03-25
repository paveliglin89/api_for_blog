# Generated by Django 2.2.16 on 2022-03-25 08:02

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0004_auto_20220325_1156'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique_users',
        ),
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together={('user', 'following')},
        ),
    ]