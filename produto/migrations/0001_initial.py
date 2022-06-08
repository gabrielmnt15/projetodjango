# Generated by Django 4.0.5 on 2022-06-08 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('codigo', models.CharField(max_length=100)),
                ('valor', models.FloatField()),
                ('quantidade', models.IntegerField()),
                ('classe', models.CharField(max_length=100)),
            ],
        ),
    ]
