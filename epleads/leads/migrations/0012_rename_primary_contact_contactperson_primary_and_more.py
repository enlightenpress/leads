# Generated by Django 4.0.1 on 2022-01-31 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0011_alter_centre_gov_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactperson',
            old_name='primary_contact',
            new_name='primary',
        ),
        migrations.RenameField(
            model_name='email',
            old_name='primary_email',
            new_name='primary',
        ),
        migrations.RenameField(
            model_name='phone',
            old_name='primary_phone',
            new_name='primary',
        ),
        migrations.AlterUniqueTogether(
            name='contactperson',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='email',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='phone',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='contactperson',
            name='centre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', related_query_name='%(class)s', to='leads.centre'),
        ),
        migrations.AlterField(
            model_name='email',
            name='centre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', related_query_name='%(class)s', to='leads.centre'),
        ),
        migrations.AlterField(
            model_name='email',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='email',
            name='person',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='emails', related_query_name='email', to='leads.contactperson'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='centre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', related_query_name='%(class)s', to='leads.centre'),
        ),
        migrations.AlterUniqueTogether(
            name='contactperson',
            unique_together={('centre', 'primary')},
        ),
        migrations.AlterUniqueTogether(
            name='email',
            unique_together={('centre', 'primary')},
        ),
        migrations.AlterUniqueTogether(
            name='phone',
            unique_together={('centre', 'primary')},
        ),
    ]
