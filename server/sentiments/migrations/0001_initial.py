# Generated by Django 4.2.7 on 2023-11-22 15:16

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sentiment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', model_utils.fields.StatusField(choices=[('unspecified', 'unspecified'), ('specified', 'specified')], default='unspecified', max_length=100, no_check_for_status=True, verbose_name='status')),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='status', verbose_name='status changed')),
                ('description', models.TextField()),
                ('sentiment_type', models.CharField(choices=[('positive', '낙관적'), ('negative', '비관적'), ('neutral', '중립적')], default='neutral', max_length=20, verbose_name='투자 심리 상태')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
