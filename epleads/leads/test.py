from pydoc import describe
from django.test import TestCase
from datetime import time
from .models import OpeningHours, Centre, Email, DataSource

# Create your tests here.
class OpeningHoursTest(TestCase):
    def setUp(self) -> None:
        source = DataSource.objects.create(source="Source", description="None")
        centre1 = Centre.objects.create(name="Test Centre 1", type=Centre.CHILDCARE)
        centre2 = Centre.objects.create(name="Test Centre 2", type=Centre.CHILDCARE)
        OpeningHours.objects.create(start_time=time(8), end_time=time(15), source=source, days=OpeningHours.MON_FRI, centre=centre1)
        OpeningHours.objects.create(start_time=time(8), end_time=time(15), source=source, days=(OpeningHours.WEEKDAYS.mon + OpeningHours.WEEKDAYS.tue), centre=centre2)
        OpeningHours.objects.create(start_time=time(10), end_time=time(14), source=source, days=(OpeningHours.WEEKDAYS.sat + OpeningHours.WEEKDAYS.sun), centre=centre2)

    def test_days_array(self):
        centre1 = Centre.objects.get(name="Test Centre 1")
        centre2 = Centre.objects.get(name="Test Centre 2")
        mon_to_fri = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        mon_tue = ['Monday', 'Tuesday']
        sat_sun = ['Saturday', 'Sunday']
        self.assertEqual(centre1.opening_hours.get().weekdays, mon_to_fri)
        self.assertEqual(centre2.opening_hours.all()[0].weekdays, mon_tue)
        self.assertEqual(centre2.opening_hours.all()[1].weekdays, sat_sun)
        
class PrimaryEmailTest(TestCase):
    def setUp(self) -> None:
        centre1 = Centre.objects.create(name="Test Centre 1", type=Centre.CHILDCARE)
        email = Email.objects.create(email='test@centre.com', primary=True, centre=centre1)
        email2 = Email.objects.create(email='test2@centre.com', centre=centre1)

        centre2 = Centre.objects.create(name="Test Centre 2", type=Centre.CHILDCARE)
        email3 = Email.objects.create(email='test3@centre.com', centre=centre2)

        centre3 = Centre.objects.create(name="Test Centre 3", type=Centre.CHILDCARE)
        email4 = Email.objects.create(email='test4@centre.com', centre=centre3)
        email5 = Email.objects.create(email='test5@centre.com', centre=centre3)

    def test_change_primary(self):
        centre1 = Centre.objects.get(name="Test Centre 1")
        email2 = Email.objects.get(email='test2@centre.com')
        email1 = Email.objects.get(email='test@centre.com')
        centre1.primary_email = email2

        email2 = Email.objects.get(email='test2@centre.com')
        email1 = Email.objects.get(email='test@centre.com')
        self.assertEqual(centre1.primary_email, email2)
        self.assertEqual(email1.primary, None)

    def test_no_primary_specified(self):
        centre2 = Centre.objects.get(name="Test Centre 2")
        email3 = Email.objects.get(email='test3@centre.com')
        self.assertEqual(centre2.emails.count(), 1)
        self.assertEqual(email3.primary, True)
        self.assertEqual(centre2.primary_email, email3)

    def test_multiple_email_no_primary(self):
        centre = Centre.objects.get(name="Test Centre 3")
        self.assertEqual(centre.emails.count(), 2)
        self.assertNotEqual(centre.primary_email, None)
        
        email = Email.objects.get(email='test4@centre.com')
        self.assertEqual(email.primary, True)
