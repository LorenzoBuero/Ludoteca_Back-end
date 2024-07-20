# Generated by Django 5.0.7 on 2024-07-19 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resenias', '0012_alter_project_options_remove_project_actualizado_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-creado'], 'verbose_name': 'Reseña', 'verbose_name_plural': 'Reseñas'},
        ),
        migrations.AddField(
            model_name='project',
            name='actualizado',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de modificación: '),
        ),
        migrations.AddField(
            model_name='project',
            name='aside_creador',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='aside_dato_curioso',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='aside_generos',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='aside_pais_origen',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='aside_plataformas',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='creado',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación: '),
        ),
        migrations.AddField(
            model_name='project',
            name='imagen_1',
            field=models.ImageField(null=True, upload_to='resenias', verbose_name='imagen 1'),
        ),
        migrations.AddField(
            model_name='project',
            name='imagen_2',
            field=models.ImageField(null=True, upload_to='resenias', verbose_name='imagen 2'),
        ),
        migrations.AddField(
            model_name='project',
            name='imagen_caratula',
            field=models.ImageField(null=True, upload_to='resenias', verbose_name='imagen de la caratula'),
        ),
        migrations.AddField(
            model_name='project',
            name='nota',
            field=models.CharField(max_length=10, null=True, verbose_name='nota'),
        ),
        migrations.AddField(
            model_name='project',
            name='parrafo_1',
            field=models.TextField(null=True, verbose_name='primer parrafo'),
        ),
        migrations.AddField(
            model_name='project',
            name='parrafo_2',
            field=models.TextField(null=True, verbose_name='segundo parrafo'),
        ),
        migrations.AddField(
            model_name='project',
            name='sintesis',
            field=models.TextField(null=True, verbose_name='síntesis'),
        ),
        migrations.AddField(
            model_name='project',
            name='subtitulo_1',
            field=models.CharField(max_length=200, null=True, verbose_name='subtitulo 1'),
        ),
        migrations.AddField(
            model_name='project',
            name='subtitulo_2',
            field=models.CharField(max_length=200, null=True, verbose_name='subtitulo 2'),
        ),
        migrations.AddField(
            model_name='project',
            name='titulo',
            field=models.CharField(max_length=100, null=True, verbose_name='título'),
        ),
    ]
