# Generated by Django 4.0 on 2021-12-27 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_alter_clasaprincipala_workout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
