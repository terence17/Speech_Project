# Generated by Django 3.1.7 on 2021-03-08 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0004_auto_20210308_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='choice_text',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AddField(
            model_name='question',
            name='choice_text2',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
    ]
