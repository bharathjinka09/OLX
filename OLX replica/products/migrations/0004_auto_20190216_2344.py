# Generated by Django 2.0.5 on 2019-02-16 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='email',
            new_name='contact_email',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='phone',
            new_name='contact_phone',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='', max_length=20),
        ),
    ]
