# Generated by Django 3.1.7 on 2021-02-26 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('date_of_birth', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Speech',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('date', models.DateTimeField()),
                ('body', models.TextField()),
                ('speaker', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='speeches.speaker')),
            ],
        ),
    ]
