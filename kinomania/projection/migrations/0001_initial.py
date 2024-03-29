# Generated by Django 4.2.9 on 2024-03-04 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0001_initial'),
        ('halls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('hour', models.TimeField()),
                ('slug', models.SlugField(blank=True, editable=False, max_length=120, unique=True)),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='halls.halls')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row_n', models.CharField()),
                ('seat_n', models.CharField()),
                ('is_taken', models.BooleanField(default=False)),
                ('projection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projection.projection')),
            ],
        ),
    ]
