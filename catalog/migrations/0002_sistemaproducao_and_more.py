# Generated by Django 5.2.1 on 2025-05-20 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SistemaProducao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='historicopropriedade',
            name='sistemas_de_producao',
        ),
        migrations.AddField(
            model_name='historicopropriedade',
            name='sistemasDeProducao',
            field=models.ManyToManyField(to='catalog.sistemaproducao'),
        ),
    ]
