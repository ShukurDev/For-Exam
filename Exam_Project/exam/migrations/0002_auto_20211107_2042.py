# Generated by Django 3.2.9 on 2021-11-07 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='quantity',
            new_name='jami_soni',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='productid',
            new_name='product',
        ),
    ]