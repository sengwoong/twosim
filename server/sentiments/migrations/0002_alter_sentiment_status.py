# Generated by Django 4.2.7 on 2023-11-26 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentiments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentiment',
            name='status',
            field=models.CharField(choices=[('unspecified', 'unspecified'), ('specified', 'specified')], default='unspecified', max_length=20),
        ),
    ]
