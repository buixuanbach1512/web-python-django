# Generated by Django 4.1.4 on 2022-12-26 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_alter_category_cat_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
