# Generated by Django 3.2.8 on 2023-09-04 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectlist_app', '0002_auto_20230904_1120'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='projecto', to='projectlist_app.category'),
            preserve_default=False,
        ),
    ]
