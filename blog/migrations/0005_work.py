# Generated by Django 2.2.12 on 2020-08-21 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_education'),
    ]

    operations = [
        migrations.CreateModel(
            name='work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
    ]
