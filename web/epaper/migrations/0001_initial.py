# Generated by Django 3.2.5 on 2023-05-08 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EPaperEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': '電子報訂閱',
                'verbose_name_plural': '電子報訂閱',
            },
        ),
    ]