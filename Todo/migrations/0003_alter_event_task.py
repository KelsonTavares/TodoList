# Generated by Django 4.2.3 on 2023-08-06 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0002_remove_event_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='task',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Todo.task'),
        ),
    ]