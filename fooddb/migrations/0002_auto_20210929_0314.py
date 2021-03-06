# Generated by Django 3.2.6 on 2021-09-29 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fooddb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='salt',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='food',
            name='sat_fats',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='food',
            name='serving_size',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='food',
            name='sugars',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
    ]
