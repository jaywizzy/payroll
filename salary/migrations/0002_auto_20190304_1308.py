# Generated by Django 2.1.7 on 2019-03-04 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salary', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salary',
            old_name='total',
            new_name='gross_pay',
        ),
        migrations.RenameField(
            model_name='salary',
            old_name='amount',
            new_name='net_pay',
        ),
    ]
