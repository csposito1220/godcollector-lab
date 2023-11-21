# Generated by Django 4.2.7 on 2023-11-21 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='God',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('description', models.TextField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Mythology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('gods', models.ManyToManyField(to='main_app.god')),
            ],
        ),
    ]
