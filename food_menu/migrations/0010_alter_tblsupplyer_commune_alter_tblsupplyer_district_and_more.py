# Generated by Django 4.1.4 on 2023-01-16 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food_menu', '0009_alter_tblsupplyer_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tblsupplyer',
            name='commune',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='commune', to='food_menu.tblcommunce', to_field='uniqid'),
        ),
        migrations.AlterField(
            model_name='tblsupplyer',
            name='district',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='district', to='food_menu.tbldistrict', to_field='uniqid'),
        ),
        migrations.AlterField(
            model_name='tblsupplyer',
            name='province',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='province', to='food_menu.tblprovince', to_field='uniqid'),
        ),
        migrations.AlterField(
            model_name='tblsupplyer',
            name='village',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='village', to='food_menu.tblvillages', to_field='uniqid'),
        ),
    ]