from contextlib import AbstractAsyncContextManager
from enum import unique
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from library.bitchoices import BitChoices
from django.core.exceptions import ObjectDoesNotExist
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models import Count

import datetime

# Create your models here.
class DataSource(models.Model):
    source = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return "%s" % self.source
    
class CentreType(models.Model):
    subtype = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.subtype

class CentreGroup(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
    )
    description = models.TextField()

    def __str__(self) -> str:
        return self.name

class GovBody(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True
    )
    description = models.TextField()

    class Meta:
        verbose_name = 'governing body'
        verbose_name_plural = 'governing bodies'

    def __str__(self) -> str:
        return self.name

class Centre(models.Model):
    SCHOOL = 'SC'
    CHILDCARE = 'CC'
    TYPE_CHOICES = [
        (SCHOOL, 'School'),
        (CHILDCARE, 'Childcare'),
    ]

    name = models.CharField(max_length=200)
    type = models.CharField(
        max_length=2,
        choices=TYPE_CHOICES,
    )
    website = models.CharField(max_length=400, blank=True)
    id_sheets = models.CharField(
        'google sheets id',
        max_length=14, 
        unique=True, 
        blank=True, 
        null=True,
    )
    google_place_id = models.CharField(
        max_length=200, 
        # unique=True,
        blank=True,
        null=True, 
    )
    gov_id = models.CharField(
        'governing body id', 
        max_length=20, 
        null=True, 
        blank=True
    )
    gov_body = models.ForeignKey(
        GovBody,
        on_delete=models.PROTECT,
        null=True,
        related_name='centres',
        related_query_name='centre',
        verbose_name='governing body',
    )
    age_range = models.CharField(max_length=20, blank=True)
    pupil_count = models.PositiveIntegerField(
        'number of pupils', 
        null=True,
        blank=True,
    )
    subtype = models.ForeignKey(
        CentreType,
        models.SET_NULL,
        blank=True,
        null=True,
        related_name='centres',
        related_query_name='centre',
    )
    group = models.ForeignKey(
        CentreGroup,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='centres',
        related_query_name='centre',
    )
    active = models.BooleanField(default=True)
    slug = models.SlugField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['gov_id', 'gov_body']

    def is_school(self):
        return self.type == self.SCHOOL
    
    def is_childcare(self):
        return self.type == self.CHILDCARE

    @property
    def primary_address(self):
        try:
            return self.addresses.filter(type=AddressType.primary_type()).get()
        except ObjectDoesNotExist:
            try:
                self.addresses.all()[0]
            except:
                return None
    
    @property
    def primary_phone(self):
        try:
            return self.phones.filter(primary = True).get()
        except ObjectDoesNotExist:
            return None


    @property
    def primary_email(self):
        try:
            return self.emails.filter(primary=True).get()
        except ObjectDoesNotExist:
            return None

    @primary_email.setter
    def primary_email(self, email):
        if email.centre == None:
            self.emails.add(email)
        elif email.centre.id != self.id:
            return
        
        p_email = self.primary_email
        p_email.primary = None
        p_email.save()

        email.primary = True
        email.save()

    @property
    def primary_contact_person(self):
        try:
            return self.contactpersons.filter(primary=True).get()
        except ObjectDoesNotExist:
            return None
    
    def __str__(self) -> str:
        return "%s (%s)" % (self.name, self.type)

class AbstractContactDetail(models.Model):
    centre = models.ForeignKey(
        Centre,
        on_delete=models.CASCADE,
        related_name="%(class)ss",
        related_query_name="%(class)s",
    )
    primary = models.BooleanField(null=True, blank=True)

    def clean(self):
        if self.primary == False or self.primary == None:
            if self.count_for_centre(self.centre) < 1:
                self.primary = True

        # return super.clean()

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
    
    @classmethod
    def count_for_centre(cls, centre):
        return cls.objects.filter(centre=centre).count()

    class Meta:
        abstract = True
        unique_together = ('centre', 'primary')

class ContactPersonPosition(models.Model):
    position = models.CharField(
        max_length=200,
        unique=True,
    )

    def __str__(self) -> str:
        return "%s" % self.position

class ContactPerson(AbstractContactDetail):
    name = models.CharField(max_length=200)
    source = models.ForeignKey(
        DataSource,
        models.SET_NULL,
        null=True,
        blank=False,
        related_name='contact_persons',
        related_query_name='contact_person',
    )
    position = models.ForeignKey(
        'ContactPersonPosition',
        on_delete=models.PROTECT,
        related_name='+'
        # default=ContactPersonPosition.get_default_pk(),
    )
    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return "%s - %s" % (self.name, self.position)


class OpeningHours(models.Model):
    MON_FRI = 31

    WEEKDAYS = BitChoices((
        ('mon', 'Monday'), 
        ('tue', 'Tuesday'), 
        ('wed', 'Wednesday'),
        ('thu', 'Thursday'), 
        ('fri', 'Friday'), 
        ('sat', 'Saturday'),
        ('sun', 'Sunday'),
    ))
    
    start_time = models.TimeField()
    end_time = models.TimeField()
    days = models.PositiveIntegerField(choices=WEEKDAYS)
    centre = models.ForeignKey(
        Centre,
        on_delete=models.CASCADE,
        related_name="opening_hours",
    )
    source = models.ForeignKey(
        DataSource,
        on_delete=models.PROTECT,
        related_name='+'
    )
    @property
    def weekdays(self):
        return self.WEEKDAYS.get_selected_values(self.days)

    def _start_to_end(self):
        return '%s - %s' % (self.start_time, self.end_time)
    
    @classmethod
    def parse_sheets_string(cls, str, ds):
        lines = str.split('\n')
        if len(lines) < 1:
            return None
        hours = {}
        for line in lines:
            parts = line.split(':')
            if len(parts) != 2:
                continue
            day= parts[0].lower()
            times= parts[1]
            
            if times not in hours:
                hours[times] = cls.day_to_int(day)
            else:
                hours[times] += cls.day_to_int(day)
        
        opening_hours = []
        for time in hours:
            parts = time.split('-')
            if len(parts) != 2:
                return None

            start = parts[0].strip()
            end = parts[1].strip()

            if len(start) != 4 or len(end) != 4:
                return None

            start_time = datetime.time(int(start[:2]), int(start[-2:]), 0)
            end_time = datetime.time(int(end[:2]), int(end[-2:]), 0)
            oh = cls(days=hours[time], source=ds, start_time=start_time, end_time=end_time)

            print(oh)

            opening_hours.append(oh)
        
        return opening_hours

    @classmethod
    def day_to_int(cls, day) -> int:
        day = day.lower()
        days = {
            'mon': 1,
            'tue': 2,
            'wed': 4,
            'thu': 8,
            'fri': 16,
            'sat': 32,
            'sun': 64,
        }

        return days[day]

    def __str__(self) -> str:
        if self.weekdays == self.MON_FRI:
            return "%s Monday to Friday" % self._start_to_end()
        return "%s on %s" % (self._start_to_end(), self.weekdays)

class NoContact(models.Model):
    from_date = models.DateField()
    to_date = models.DateField(
        null=True,
        blank=True,
    )
    status = models.CharField(max_length=100)
    centre = models.OneToOneField(
        Centre,
        on_delete=models.CASCADE,
        related_name='no_contact',
        primary_key=True,
    )
    requsted_by = models.ForeignKey(
        ContactPerson,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+',
    )
    reason=models.TextField()

    def is_active(self):
        if self.to_date < datetime.date.today:
            return False
        
        return True
    
    def __str__(self) -> str:
        if self.to_date is None:
            return "No contact since %s" % self.from_date
        
        if self.to_date < datetime.date.today:
            return "No contact period has ended"
        
        return "No contact since %s until %s" % (self.from_date, self.to_date)

class Country(models.Model):
    code = models.CharField(
        max_length=2, 
        unique=True, 
        primary_key=True,
    )
    name = models.CharField(max_length=60)

    def __str__(self) -> str:
        return "%s (%s)" % (self.name, self.code)
    
    class Meta:
        verbose_name_plural = 'countries'
    
class Phone(AbstractContactDetail):
    MOBILE = 'mob'
    LANDLINE = 'lan'
    DISCONNECTED = 'dis'
    INACTIVE = 'ina'

    TYPE_CHOICES = [
        (MOBILE, 'Mobile'),
        (LANDLINE, 'Landline'),
        (DISCONNECTED, 'Disconnected'),
        (INACTIVE, 'Inactive'),
    ]

    country = models.ForeignKey(
        Country,
        on_delete=models.PROTECT,
        related_name='+',
    )
    number = PhoneNumberField()
    type = models.CharField(
        max_length=3,
        choices=TYPE_CHOICES,
    )
    person = models.ForeignKey(
        ContactPerson,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='phones',
        related_query_name='phone',
    )
    source = models.ForeignKey(
        DataSource,
        models.SET_NULL,
        null=True,
        blank=False,
        related_name='phones',
        related_query_name='phones',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def local_number(self):
        return self.number.as_national

    @property
    def is_active(self):
        return self.type in (self.DISCONNECTED, self.INACTIVE)
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super(Phone, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.local_number

class Email(AbstractContactDetail):
    email = models.EmailField()
    source = models.ForeignKey(
        DataSource,
        models.SET_NULL,
        null=True,
        blank=False,
        related_name='emails',
        related_query_name='email',
    )
    is_active = models.BooleanField(
        default=True,
    )
    person = models.ForeignKey(
        ContactPerson,
        on_delete=models.SET_NULL,
        default=None,
        null=True,
        blank=True,
        related_name='emails',
        related_query_name='email',
    )
    source = models.ForeignKey(
        DataSource,
        models.SET_NULL,
        null=True,
        blank=False,
        related_name='emails',
        related_query_name='email',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return "%s" % self.email

class AddressType(models.Model):
    type = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    @classmethod
    def primary_type(cls):
       return cls.objects.get_or_create(type='Physical Address')[0] 


    def __str__(self) -> str:
        return "%s" % self.type

class Address(models.Model):
    address = models.CharField('street address', max_length=500)
    city = models.CharField('city / suburb / local area', max_length=200)
    state = models.CharField('state / district / region', max_length=200)
    postcode = models.CharField(max_length=20)
    country = models.ForeignKey(
        Country,
        models.PROTECT,
        related_name='+',
    )
    lattitude = models.DecimalField(max_digits=8, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    type = models.ForeignKey(
        AddressType,
        models.PROTECT,
        related_name='+',
    )
    centre = models.ForeignKey(
        Centre,
        models.CASCADE,
        related_name='addresses',
        related_query_name='address',
    )
    source = models.ForeignKey(
        DataSource,
        models.SET_NULL,
        null=True,
        blank=False,
        related_name='addresses',
        related_query_name='address',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def latlong(self):
        return "%s, %s" % (self.lattitude, self.longitude)

    class Meta:
        verbose_name_plural = 'addresses'
        unique_together = ['centre','type']

    def __str__(self) -> str:
        return "%s, %s, %s, %s, %s" % (self.address, self.city, self.state, self.postcode, self.country)
