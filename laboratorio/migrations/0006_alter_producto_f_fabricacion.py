# Generated by Django 5.1.3 on 2024-11-27 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0005_producto_f_fabricacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='f_fabricacion',
            field=models.IntegerField(choices=[(2015, '2015'), (2016, '2016'), (2017, '2017'), (2018, '2018'), (2019, '2019'), (2020, '2020'), (2021, '2021'), (2022, '2022'), (2023, '2023'), (2024, '2024')], default=2024, verbose_name='F Fabricación'),
        ),
    ]
