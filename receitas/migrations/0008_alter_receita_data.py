# Generated by Django 4.1.3 on 2022-11-07 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0007_delete_despesa_remove_receita_ano_remove_receita_dia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='data',
            field=models.DateField(),
        ),
    ]