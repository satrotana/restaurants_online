# Generated by Django 4.1.4 on 2023-01-05 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food_menu', '0002_rename_description_tblvillages_khmer'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='tblprovinc',
            new_name='tblprovince',
        ),
        migrations.RenameField(
            model_name='tblcustomer',
            old_name='auth',
            new_name='inputer',
        ),
    ]
