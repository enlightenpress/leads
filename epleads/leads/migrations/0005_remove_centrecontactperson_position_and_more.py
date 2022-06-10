# Generated by Django 4.0.1 on 2022-01-12 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0004_centre_p_address_centre_p_email_centre_p_person_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='centrecontactperson',
            name='position',
        ),
        migrations.AddField(
            model_name='contactperson',
            name='position',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='leads.contactpersonposition'),
            preserve_default=False,
        ),
    ]