# Generated by Django 4.0.3 on 2022-06-15 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BinVO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('closet_name', models.CharField(max_length=150)),
                ('import_href', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=150)),
                ('model_name', models.CharField(max_length=150)),
                ('color', models.CharField(max_length=150)),
                ('picture_url', models.URLField(null=True)),
                ('bin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shoes', to='shoes_rest.binvo')),
            ],
        ),
    ]
