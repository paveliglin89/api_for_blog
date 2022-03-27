# Generated by Django 2.2.16 on 2022-03-27 21:22

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20220327_1018'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.CheckConstraint(check=models.Q(_negated=True, user=django.db.models.expressions.F('following')), name='could_not_follow_yourself'),
        ),
    ]