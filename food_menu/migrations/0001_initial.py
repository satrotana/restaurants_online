# Generated by Django 4.1.4 on 2023-01-26 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tblcommunce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniqid', models.CharField(max_length=50, null=True, unique=True)),
                ('khmer', models.CharField(max_length=255, null=True)),
                ('english', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'tblcommunce',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='tblcustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=200)),
                ('last_name', models.CharField(blank=True, max_length=200)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('mobile', models.CharField(blank=True, max_length=200)),
                ('image', models.ImageField(blank=True, default='user.png', upload_to='customer')),
                ('input_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'tblcustomer',
            },
        ),
        migrations.CreateModel(
            name='tbldistrict',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniqid', models.CharField(max_length=50, null=True, unique=True)),
                ('khmer', models.CharField(max_length=255, null=True)),
                ('english', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'tbldistrict',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='tblprovince',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniqid', models.CharField(max_length=50, null=True, unique=True)),
                ('khmer', models.CharField(max_length=255, null=True)),
                ('english', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'tblprovince',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='tblvillages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniqid', models.CharField(max_length=50, null=True, unique=True)),
                ('khmer', models.CharField(max_length=255, null=True)),
                ('english', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'tblvillages',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='tblsupplyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('mobile', models.CharField(blank=True, max_length=200, null=True)),
                ('company_name', models.CharField(blank=True, max_length=225, null=True)),
                ('image', models.ImageField(blank=True, default='user.png', upload_to='supplyer')),
                ('input_date', models.DateTimeField(auto_now=True)),
                ('commune', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='commune', to='food_menu.tblcommunce', to_field='uniqid')),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='district', to='food_menu.tbldistrict', to_field='uniqid')),
            ],
            options={
                'db_table': 'tblsupplyer',
            },
        ),
    ]
