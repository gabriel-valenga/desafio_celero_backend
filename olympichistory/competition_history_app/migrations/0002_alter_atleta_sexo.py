# Generated by Django 3.2.9 on 2021-11-23 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition_history_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atleta',
            name='sexo',
            field=models.CharField(choices=[('F', 'Feminino'), ('M', 'Masculino'), ('O', 'Outro')], max_length=1),
        ),
    ]