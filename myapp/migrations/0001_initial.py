# Generated by Django 5.1.4 on 2025-01-22 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=10)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.TextField(max_length=100)),
            ],
        ),
    ]
