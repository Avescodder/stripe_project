# Generated by Django 5.2.1 on 2025-05-31 23:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_rename_discriprion_item_discription'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='discription',
            new_name='description',
        ),
    ]
