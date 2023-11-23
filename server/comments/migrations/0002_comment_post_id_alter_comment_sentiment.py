# Generated by Django 4.2.7 on 2023-11-23 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sentiments', '0001_initial'),
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post_id',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='sentiment',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sentiments.sentiment'),
        ),
    ]
