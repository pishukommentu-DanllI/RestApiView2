# Generated by Django 4.1.2 on 2023-03-02 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
