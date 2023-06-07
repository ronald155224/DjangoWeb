# Generated by Django 3.2.5 on 2023-05-08 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_setting_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocaleSetting',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='語言代碼')),
                ('language', models.CharField(max_length=50, verbose_name='系統語言')),
            ],
            options={
                'verbose_name': '翻譯對照表',
                'verbose_name_plural': '翻譯對照表',
            },
        ),
        migrations.CreateModel(
            name='TranslateSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raw_string', models.CharField(max_length=255, verbose_name='原始文字')),
                ('translated_string', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='翻譯後文字')),
                ('locale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translatesetting_set', to='core.localesetting')),
            ],
            options={
                'verbose_name': '翻譯文字',
                'verbose_name_plural': '翻譯文字',
                'ordering': ['raw_string'],
            },
        ),
    ]
