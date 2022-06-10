from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
import leads.models as models
from .forms import EmailForm, OpeningHoursForm, PhoneForm
from import_export.admin import ImportExportModelAdmin
from .resource import CombinedCentreResource

from scrapers.models import Scraper, ScrapeQueue

#Custom Admin Site
class EPLeadsAdminSite(AdminSite):
    site_header = 'EP Leads Administrator'

admin_site = EPLeadsAdminSite(name='myadmin')

#Register default auth admin
admin_site.register(Group, GroupAdmin)
admin_site.register(User, UserAdmin)

#Site-wide actions
# admin_site.disable_action('delete_selected')

#Register models that do not require custom admin models
admin_site.register(models.DataSource)
admin_site.register(models.GovBody)
admin_site.register(models.CentreType)
admin_site.register(models.Country)
admin_site.register(models.AddressType)
admin_site.register(models.ContactPersonPosition)
#Scraper models
admin_site.register(Scraper)
admin_site.register(ScrapeQueue)

#Centre model admin and inlines
class AddressInline(admin.StackedInline):
    model = models.Address
    extra = 0
    fields = (
        ('address', 'city', ),
        ('state', 'postcode', 'country', ),
        ('lattitude', 'longitude', ), 
        ('type', 'source', ),
    )

class PhoneInline(admin.TabularInline):
    model = models.Phone
    form = PhoneForm
    extra = 0

class EmailInline(admin.TabularInline):
    model = models.Email
    form = EmailForm
    extra = 0

class ContactPersonInline(admin.TabularInline):
    model = models.ContactPerson
    extra = 0

class NoContactInline(admin.TabularInline):
    model = models.NoContact
    extra = 0

class OpeningHours(admin.StackedInline):
    model = models.OpeningHours
    form = OpeningHoursForm

    fields = (('start_time', 'end_time'), 'days')
    extra = 0

@admin.register(models.Centre, site=admin_site)
class CentreAdmin(ImportExportModelAdmin):
    resource_class = CombinedCentreResource
    fieldsets = (
        (None, {
            'fields': (
                'name',
                ('type', 'subtype'),
                'website',
                # 'contact_persons', 
            )
        }),
        ('Advanced Options', {
            'classes': ('collapse', ),
            'fields': (
                ('id_sheets', 'gov_id', 'gov_body'), 
                ('age_range', 'pupil_count'), 
                'active', 
            )
        }),
    )
    # filter_horizontal = ['contact_persons']
    inlines=[AddressInline, PhoneInline, EmailInline, ContactPersonInline, NoContactInline, OpeningHours]
    # exclude = ('contact_persons', )
    search_fields=['name', 'address__address', 'address__city', 'address__state', 'phone__number', 'email__email', 'id_sheets']
    list_display=[
        'name', 
        'type', 
        'primary_address', 
        'primary_phone', 
        'primary_email', 
        'primary_contact_person',
        'no_contact', 
        'active'
    ]
    list_filter=['type', 'active', 'address__state']