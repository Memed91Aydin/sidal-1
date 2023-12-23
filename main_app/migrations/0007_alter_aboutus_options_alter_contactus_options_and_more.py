# Generated by Django 4.2.7 on 2023-11-24 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_delete_catalogue_delete_latestnews_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutus',
            options={'ordering': ['comapny_name'], 'verbose_name': 'About US'},
        ),
        migrations.AlterModelOptions(
            name='contactus',
            options={'ordering': ['date'], 'verbose_name': 'Contact Us'},
        ),
        migrations.AlterModelOptions(
            name='mainpagepics',
            options={'ordering': ['name'], 'verbose_name': 'Main Page Pictures'},
        ),
        migrations.AlterModelOptions(
            name='mainviewpage',
            options={'ordering': ['first_words'], 'verbose_name': 'View of Main Page'},
        ),
        migrations.AlterModelOptions(
            name='services',
            options={'ordering': ['service_name'], 'verbose_name': 'Services'},
        ),
        migrations.AlterModelOptions(
            name='socialmedialinks',
            options={'ordering': ['platform'], 'verbose_name': 'Social Media Links'},
        ),
        migrations.AddField(
            model_name='contactus',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='Message Date'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='image',
            field=models.ImageField(default='', upload_to='Images/AboutUS/%y/%m%d', verbose_name='Images About Us'),
        ),
        migrations.AlterField(
            model_name='mainpagepics',
            name='image',
            field=models.ImageField(default='', upload_to='Images/MainPage/%y/%m%d', verbose_name='Photo of Main Page'),
        ),
    ]
