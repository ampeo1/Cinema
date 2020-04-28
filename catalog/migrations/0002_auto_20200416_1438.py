# Generated by Django 3.0.5 on 2020-04-16 11:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('photo', models.ImageField(upload_to='photo_actors')),
                ('biography', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='film',
            name='description',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='FilmInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID, primary_key=True, serialize=False)),
                ('film', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Film')),
            ],
        ),
        migrations.AddField(
            model_name='film',
            name='actors',
            field=models.ManyToManyField(help_text='Выберите актёров', to='catalog.Actor'),
        ),
        migrations.AddField(
            model_name='film',
            name='genre',
            field=models.ManyToManyField(help_text='Выберите жанр фильм', to='catalog.Genre'),
        ),
    ]
