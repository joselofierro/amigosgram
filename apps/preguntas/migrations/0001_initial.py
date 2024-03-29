# Generated by Django 2.1.4 on 2019-01-23 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=200)),
                ('fecha', models.DateField(verbose_name='Fecha de publicación')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='preguntas', to='categorias.Categoria')),
            ],
        ),
    ]
