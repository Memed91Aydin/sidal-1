# Generated by Django 4.2.7 on 2023-12-11 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0026_alter_dodinkjet_type_alter_lasermarkinginkjet_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lasermarkinginkjet',
            name='type',
            field=models.CharField(choices=[('uv', 'uv'), ('fiber', 'fiber'), ('co2', 'co2')], max_length=50),
        ),
    ]
