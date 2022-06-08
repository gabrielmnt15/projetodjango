# Generated by Django 4.0.5 on 2022-06-08 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='nota_fiscal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf_comprador', models.CharField(max_length=11)),
                ('cnpj_fornecedor', models.CharField(max_length=14)),
                ('valor_compra', models.FloatField()),
                ('produto', models.CharField(max_length=100)),
            ],
        ),
    ]