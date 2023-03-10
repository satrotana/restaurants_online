# Generated by Django 4.1.4 on 2023-01-27 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food_menu', '0002_initial'),
        ('users', '0003_user_province'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='commune',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='commune_us', to='food_menu.tblcommunce', to_field='uniqid'),
        ),
        migrations.AddField(
            model_name='user',
            name='district',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='district_us', to='food_menu.tbldistrict', to_field='uniqid'),
        ),
        migrations.AddField(
            model_name='user',
            name='village',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='village_us', to='food_menu.tblvillages', to_field='uniqid'),
        ),
    ]
