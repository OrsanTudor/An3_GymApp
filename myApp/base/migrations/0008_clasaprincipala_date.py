# Generated by Django 4.0 on 2021-12-27 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_remove_clasaprincipala_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='clasaprincipala',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
