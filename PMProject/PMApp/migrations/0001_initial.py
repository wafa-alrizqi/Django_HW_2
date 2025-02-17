# Generated by Django 4.0.4 on 2022-05-23 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the project.', max_length=100)),
                ('creation_time', models.DateTimeField(auto_now_add=True, help_text='Date the project was created.')),
                ('completion_time', models.DateTimeField(help_text='Date the project was completed.', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Task Title', max_length=100)),
                ('description', models.TextField(help_text='Task description')),
                ('time_estimate', models.IntegerField(help_text=' Task estimated time')),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
