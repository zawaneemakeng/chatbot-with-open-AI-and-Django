# Generated by Django 3.2 on 2023-01-15 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatchat', '0003_product'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.AlterField(
            model_name='qa2',
            name='qa',
            field=models.CharField(max_length=1000),
        ),
    ]