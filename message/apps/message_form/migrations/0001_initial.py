# Generated by Django 2.2 on 2022-08-08 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='message',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='user name')),
                ('email', models.EmailField(max_length=254, verbose_name='email address')),
                ('address', models.CharField(max_length=100, verbose_name='address')),
                ('message', models.TextField(verbose_name='message')),
            ],
            options={
                'verbose_name': 'message',
                'verbose_name_plural': 'message',
                'db_table': 'message',
            },
        ),
    ]

