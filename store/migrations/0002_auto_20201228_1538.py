# Generated by Django 3.1.4 on 2020-12-28 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='title',
            new_name='name',
        ),
    ]