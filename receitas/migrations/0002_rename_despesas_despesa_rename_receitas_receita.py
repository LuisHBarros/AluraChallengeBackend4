# Generated by Django 4.1.3 on 2022-11-02 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Despesas',
            new_name='Despesa',
        ),
        migrations.RenameModel(
            old_name='Receitas',
            new_name='Receita',
        ),
    ]