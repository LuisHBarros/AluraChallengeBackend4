# Generated by Django 4.1.3 on 2022-11-07 14:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0006_remove_receita_data_receita_ano_receita_dia_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Despesa',
        ),
        migrations.RemoveField(
            model_name='receita',
            name='ano',
        ),
        migrations.RemoveField(
            model_name='receita',
            name='dia',
        ),
        migrations.RemoveField(
            model_name='receita',
            name='mes',
        ),
        migrations.AddField(
            model_name='receita',
            name='data',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='receita',
            name='descricao',
            field=models.CharField(max_length=255, unique_for_month='data'),
        ),
    ]
