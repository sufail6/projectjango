# Generated by Django 4.1.1 on 2022-09-16 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app123', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=25)),
                ('description', models.TextField()),
            ],
        ),
    ]