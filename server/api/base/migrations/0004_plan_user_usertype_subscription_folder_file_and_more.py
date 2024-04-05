# Generated by Django 5.0.3 on 2024-04-02 11:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_advocate_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('plan_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('cost', models.BigIntegerField(max_length=200)),
                ('duration', models.CharField(max_length=200)),
                ('deleted', models.IntegerField(default=0, max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('profession', models.CharField(max_length=200)),
                ('deleted', models.IntegerField(default=0, max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Usertype',
            fields=[
                ('usertype_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('usertype_name', models.CharField(max_length=200)),
                ('deleted', models.IntegerField(default=0, max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.user')),
            ],
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('folder_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('folder_name', models.CharField(max_length=200)),
                ('deleted', models.IntegerField(default=0, max_length=1)),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.user')),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('file_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('path', models.TextField(blank=True, max_length=250, null=True)),
                ('deleted', models.IntegerField(default=0, max_length=1)),
                ('folder_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.folder')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.user')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='usertype_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.usertype'),
        ),
    ]
