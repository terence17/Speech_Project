# Generated by Django 3.1.7 on 2021-03-07 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='choice_text2',
            field=models.CharField(default='Yes', max_length=200),
        ),
    ]
