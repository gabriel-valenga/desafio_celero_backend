# Generated by Django 3.2.9 on 2021-11-24 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition_history_app', '0003_auto_20211124_0854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competicaoatleta',
            name='medalha',
            field=models.CharField(blank=True, choices=[('Golden', 'Ouro'), ('Silver', 'Prata'), ('Bronze', 'Bronze'), ('NA', 'Sem medalha')], max_length=6),
        ),
    ]