# Generated by Django 4.2.1 on 2023-05-22 09:52

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CartoonUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25)),
                ('surname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Cartoon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('author', models.CharField(default='default', max_length=20)),
                ('country',
                 models.CharField(choices=[('US', 'America'), ('EU', 'Europe'), ('UA', 'Ukraine')], default='O',
                                  max_length=2)),
                ('year', models.PositiveIntegerField(default=1900,
                                                     validators=[django.core.validators.MinValueValidator(1901),
                                                                 django.core.validators.MaxValueValidator(2025)])),
                ('rating', models.PositiveIntegerField(default=0,
                                                       validators=[django.core.validators.MinValueValidator(1),
                                                                   django.core.validators.MaxValueValidator(100)])),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE,
                                           to='nickelodeon.cartoonuser')),
            ],
        ),
    ]
