# Generated by Django 5.0.3 on 2024-03-28 08:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='advocate',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.company'),
        ),
    ]
