# Generated by Django 4.0.1 on 2022-01-20 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0010_alter_contactperson_primary_contact_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CentreGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='centre',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='centres', related_query_name='centre', to='leads.centregroup'),
        ),
    ]