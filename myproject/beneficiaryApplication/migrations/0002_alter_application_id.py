# Generated by Django 4.0.6 on 2022-08-02 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiaryApplication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
