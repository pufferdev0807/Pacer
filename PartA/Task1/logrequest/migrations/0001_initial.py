# Generated by Django 4.1.2 on 2022-10-11 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_ID', models.CharField(max_length=20, verbose_name='User Id')),
                ('Score', models.CharField(max_length=20, verbose_name='Score')),
            ],
        ),
    ]
