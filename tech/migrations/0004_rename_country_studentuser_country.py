# Generated by Django 4.1 on 2022-09-01 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0003_posts_sub_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentuser',
            old_name='Country',
            new_name='country',
        ),
    ]
