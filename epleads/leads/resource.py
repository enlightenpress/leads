
from ast import Add
from import_export import resources, widgets, fields
import phonenumbers
from phonenumber_field.phonenumber import PhoneNumber
from .models import AddressType, Centre, ContactPersonPosition, Email, OpeningHours, Phone, Address, ContactPerson, DataSource, Country
import logging

logger = logging.getLogger('import_export')
# class EmailWidget(widgets.ForeignKeyWidget):    
    # get_queryset()

class EmailResource(resources.ModelResource):
    centre = fields.Field(
        column_name='centre',
        attribute='centre',
        widget=widgets.ForeignKeyWidget(Centre, 'id_sheets')
    )
    
    class Meta:
        model = Email
        skip_unchanged = True
        exclude = ('updated_at', 'created_at',)

class AddressResource(resources.ModelResource):
    centre = fields.Field(
        column_name='centre',
        attribute='centre',
        widget=widgets.ForeignKeyWidget(Centre, 'id_sheets')
    )
    address_type = fields.Field(
        column_name='type',
        attribute='type',
        widget=widgets.ForeignKeyWidget(AddressType, 'pk')
    )
    
    class Meta:
        model = Address
        skip_unchanged = True
        exclude = ('updated_at', 'created_at',)

class PhoneResource(resources.ModelResource):
    centre = fields.Field(
        column_name='centre',
        attribute='centre',
        widget=widgets.ForeignKeyWidget(Centre, 'id_sheets')
    )
    source = fields.Field(
        column_name="source",
        attribute="source",
        widget=widgets.ForeignKeyWidget(DataSource, 'source')
    )
    class Meta:
        model = Phone
        skip_unchanged = True
        exclude = ('updated_at', 'created_at',)

    def before_import_row(self, row, row_number=None, **kwargs):
        try:
            phone = PhoneNumber.from_string(row['number'], row['country'])
        except phonenumbers.phonenumberutil.NumberParseException:
            logger.warning("Phone number (%s) is invalid for Centre(%s)" % (row['number'], row['centre']))
            return

        row['number'] = phone.as_e164
        return super().before_import_row(row, row_number, **kwargs)
    
    def skip_row(self, instance, original):
        if not phonenumbers.is_valid_number(instance.number):
            logger.warning("Phone number (%s) is invalid for Centre(%s)" % (instance.number, instance.centre))
            return True
        return False

class ContactPersonResource(resources.ModelResource):
    centre = fields.Field(
        column_name='centre',
        attribute='centre',
        widget=widgets.ForeignKeyWidget(Centre, 'id_sheets')
    )
    class Meta:
        model = ContactPerson
        skip_unchanged = True
        exclude = ('updated_at', 'created_at',)

class OpeningHoursResource(resources.ModelResource):
    centre = fields.Field(
        column_name='centre',
        attribute='centre',
        widget=widgets.ForeignKeyWidget(Centre, 'id_sheets')
    )
    class Meta:
        model = ContactPerson
        skip_unchanged = True
        exclude = ('updated_at', 'created_at',)

class CentreResource(resources.ModelResource):
    class Meta:
        model = Centre
        skip_unchanged = True
        exclude = ('updated_at', 'created_at',)
        import_id_fields = ['id_sheets']



class CombinedCentreResource(resources.ModelResource):
    primary_email = fields.Field(
        attribute='primary_email',
        readonly=True,
        # widget=widgets.ForeignKeyWidget(Email, 'email'),
    )
    primary_phone = fields.Field(
        attribute='primary_phone',
        readonly=True,
        # widget=widgets.ForeignKeyWidget(Phone, 'local_number'),
    )
    address = fields.Field(
        attribute='primary_address__address',
        readonly=True,
        # widget=widgets.ForeignKeyWidget(Phone, 'address'),
    )
    city = fields.Field(attribute='primary_address__city', readonly=True)
    postcode = fields.Field(attribute='primary_address__postcode', readonly=True)
    country = fields.Field(attribute='primary_address__country', readonly=True)
    state = fields.Field(attribute='primary_address__state', readonly=True)
    lattitude = fields.Field(attribute='primary_address__lattitude', readonly=True)
    longitude = fields.Field(attribute='primary_address__longitude', readonly=True)
    primary_person = fields.Field(
        attribute='primary_contact_person',
        readonly=True,
        # widget=widgets.ForeignKeyWidget(ContactPerson, 'contact_person'),
    )
    emails = fields.Field(
        attribute='emails',
        readonly=True,
        widget=widgets.ManyToManyWidget(Email, separator='\n', field='email'),
    )
    phones = fields.Field(
        attribute='phones',
        readonly=True,
        widget=widgets.ManyToManyWidget(Phone, separator='\n', field='number'),
    )
    contact_person = fields.Field(
        attribute='primary_contact__name', 
        readonly=True,
    )
    position = fields.Field(
        attribute='primary_contact__position__name',
        readonly=True,
    )
    opening_hours = fields.Field(
        attribute='opening_hours',
        readonly=True,
        widget=widgets.ManyToManyWidget(Phone, separator='\n', field='number'),
    )
    class Meta:
        model = Centre
        # skip_unchanged = True
        # import_id_fields = ['sheets_id', 'gov_id', 'id']
        # report_skipped = False
        exclude = ('updated_at', 'created_at',)

    def before_import_row(self, row, row_number=None, **kwargs):
        ids = ['google_place_id', 'gov_id', 'id_sheets']
        for i in ids:
            if row[i] == '':
                row[i] = None

    def after_import_row(self, row, row_result, row_number=None, **kwargs):
        ds, ds_save = DataSource.objects.get_or_create(source='Google Sheets Import', description='')

        try:
            obj = Centre.objects.get(pk=row_result.object_id)
            logger.info("Adding details for centre: %s" % obj.name)
        except:
            logger.info("No changes made for centre: %s" % row["name"])
            return None
        
        try:
            country = row['country']
            address = row['address']
            state = row['state']
            postcode = row['postcode']
            city = row['city']
            lat = row['lattitude']
            long = row['longitude']
            add_res = self._add_address(obj, ds, address, city, state, postcode, country, lat, long)

            contact_person = row['contact_person']
            position = row['position']
            contact_res = self._add_contact_person(obj, ds, contact_person, position)

            primary_email_str = row['primary_email']
            emails_str = row['emails'].split('\n')
            email_res = self._add_emails(obj, ds, emails_str, primary_email_str)

            primary_phone_str = row['primary_phone']
            phones_str = row['phones'].split('\n')
            phones_res = self._add_phones(obj, ds, phones_str, primary_phone_str, country)

            opening_hours = row['opening_hours']
            oh_res = self._add_opening_hours(obj, ds, opening_hours)

            results = {"Address": add_res, "Contact Person": contact_res, "Emails": email_res, "Phones": phones_res, "Opening Hours": oh_res}
            message = "Details added for: "
            for res in results:
                if results[res]:
                    message = "%s %s, " % (message, res)
            logger.info(message) 

        except Exception as e:
            logger.error("%s - %s" % (row['name'], e))
            

        return super().after_import_row(row, row_result, row_number, **kwargs)
    
    def _add_opening_hours(self, obj, ds, hours_str):
        if hours_str == '' or hours_str == None:
            return None

        opening_hours = OpeningHours.parse_sheets_string(hours_str, ds)

        if not opening_hours:
            logger.error('Opening Hours not formated correctly for %s', obj.name)
            return None

        for oh in opening_hours:
            obj.opening_hours.add(oh, bulk=False)

        if opening_hours:
            return True
        
    def _add_contact_person(self, obj, ds, contact_person, position_str):
        if position_str == '' or position_str == None or contact_person == '' or contact_person ==  None:
            return None

        primary = False
        if obj.primary_contact_person == None:
            primary = True

        position, pos_save = ContactPersonPosition.objects.get_or_create(position=position_str)
        
        result = obj.contactpersons.create(
            name = contact_person,
            position = position,
            source = ds,
            primary = primary,
        )

        if result:
            return True
        
        return None

    def _add_address(self, obj, ds, address, city, state, postcode, country_code, lat, long):
        try: 
            country = Country.objects.get(code=country_code)
        except Country.DoesNotExist:
            logger.warning('No country found with country code: %s' % country_code)
            return None

        address = Address(
            address=address, 
            city=city, 
            postcode=postcode, 
            state=state,
            country=country,
            source=ds, 
            centre=obj,
            lattitude=lat,
            longitude=long,
            type=AddressType.primary_type(),
        )

        if obj.primary_address != None:
            address.id = obj.primary_address

        address.save()

        return True

    def _add_phones(self, obj, ds, phones_str, primary_phone_str, country_code):
        if phones_str == None or len(phones_str) < 1:
            return None

        primary_phone = ''
        if primary_phone_str != '' and primary_phone_str != None:
            primary_phone = PhoneNumber.from_string(phone_number=primary_phone_str, region=country_code).as_e164

        try: 
            country = Country.objects.get(code=country_code)
        except Country.DoesNotExist:
            return None

        for s in phones_str:
            if s == '' or s == None:
                continue
            phone = PhoneNumber.from_string(phone_number=s, region=country_code).as_e164
            if phone == primary_phone and not obj.phones.filter(number=phone):
                current_primary = obj.primary_phone
                if current_primary != None:
                    current_primary.primary = False
                    current_primary.save()

                obj.phones.create(
                    number=phone,
                    country=country,
                    primary=True,
                    type=Phone.LANDLINE,
                    source=ds,
                )
            elif not obj.phones.filter(number=phone):
                obj.phones.create(
                    number=phone,
                    country=country,
                    type=Phone.LANDLINE,
                    source=ds,
                )
            
        return True

    def _add_emails(self, obj, ds, emails_str, primary_email_str):
        if emails_str == None or len(emails_str) < 1:
            return None
        for s in emails_str:
            if s == '' or s == None:
                continue
            elif s == primary_email_str:
                current_primary = obj.primary_email
                if current_primary != None:
                    current_primary.primary = False
                    current_primary.save()

                obj.emails.create(
                    email=s,
                    primary=True,
                    is_active=True,
                    source=ds,
                )
            elif not obj.emails.filter(email=s):
                obj.emails.create(
                    email=s,
                    is_active=True,
                    source=ds,
                )

        return True
        