# Generated by Django 4.0.1 on 2022-02-07 01:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0017_govbody_centregroup_description_alter_centre_gov_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='centre',
            name='google_place_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='centre',
            name='gov_body',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='centres', related_query_name='centre', to='leads.govbody', verbose_name='governing body'),
        ),
        migrations.AlterField(
            model_name='centre',
            name='gov_id',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='governing body id'),
        ),
        migrations.AlterField(
            model_name='centre',
            name='website',
            field=models.CharField(blank=True, max_length=400),
        ),
    ]
