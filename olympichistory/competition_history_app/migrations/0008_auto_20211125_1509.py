# Generated by Django 3.2.9 on 2021-11-25 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competition_history_app', '0007_auto_20211125_0820'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competicao',
            name='olimpiada',
        ),
        migrations.AddField(
            model_name='competicaoatleta',
            name='olimpiada',
            field=models.ForeignKey(default='Nao Informada', on_delete=django.db.models.deletion.RESTRICT, to='competition_history_app.olimpiada', to_field='nome'),
        ),
    ]
