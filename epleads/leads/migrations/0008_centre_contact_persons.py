# Generated by Django 4.0.1 on 2022-01-13 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0007_alter_centrecontactperson_unique_together_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='centre',
            name='contact_persons',
            field=models.ManyToManyField(through='leads.CentreContactPerson', to='leads.ContactPerson'),
        ),
    ]