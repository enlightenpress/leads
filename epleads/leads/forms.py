from calendar import THURSDAY
from unittest.mock import seal
from django import forms
from .models import OpeningHours, Centre, ContactPerson, Phone, Email
# import phonenumbers
from phonenumber_field.phonenumber import PhoneNumber

# class DaysChoiceWidget(forms.MultiWidget):
#     def __init__(self, attrs=None, choices=None) -> None:
#         # monday = 1
#         # tuesday = 2
#         # wednesday = 4
#         # thursday = 8
#         # friday = 16
#         # saturday = 32
#         # sunday = 64
#         print(choices.get)
#         # widgets = [ forms.Select(attrs=attrs, choices=[x]) for x in choices]
#         super().__init__(DaysChoiceWidget, attrs)
    
#     def decompress(self, value):
#         if isinstance(value, int):
#             print(value)
#             return sum(value.monday, value.tuesday, value.wednesday, value.thursday, value.friday, value.saturday, value.sunday)
#         return 0

#     def value_from_datadict(self, data, files, name):
#         value = super(DaysChoiceWidget, self).value_from_datadict(data, files, name)
#         # print
#         # value = sum([int(x) for x in value])
#         return value

# class BitChoicesField(forms.MultipleChoiceField):
    
#     def value_from_datadict(self, data, files, name):
#         value = super(BitChoicesField, self).value_from_datadict(data, files, name)
#         # print
#         value = sum([int(x) for x in value])
#         return value

class OpeningHoursForm(forms.ModelForm):

    # days = forms.IntegerField(widget=BitChoicesField(
    #     choices=OpeningHours.WEEKDAYS
    # ))
    days = forms.MultipleChoiceField(label='Checkbox For', required=False, widget = forms.CheckboxSelectMultiple, choices=OpeningHours.WEEKDAYS)

    # def __init__(self, *args, **kwargs):
    #     # days = kwargs.pop('days', None)
    #     super(OpeningHoursForm, self).__init__(*args, **kwargs)
    #     self.fields['days'].choices = OpeningHours.WEEKDAYS

    def clean_days(self):
        days = self.cleaned_data.get("days",  False)
        
        if days is None:
            return days
        
        if isinstance(days, list):
            try:
                days_int = sum([int(x) for x in days])
                return days_int
            except:
                return days

        return days
        

    class Meta:
        model = OpeningHours
        fields = ['start_time', 'end_time', 'days', 'centre']

class PhoneForm(forms.ModelForm):
    number = forms.CharField()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'instance' in kwargs:
            phone = kwargs['instance']
            self.fields['person'].queryset = ContactPerson.objects.filter(centre=phone.centre)
    
    def clean(self):
        return super().clean()
    
    def clean_number(self):
        print(self.cleaned_data['number'], self.cleaned_data['country'].code)
        print(type(self.cleaned_data['number']))
        phone = PhoneNumber.from_string(self.cleaned_data['number'], self.cleaned_data['country'].code)
        print("Phone NUmber: %s" % phone)
        return phone


class EmailForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'instance' in kwargs:
            email = kwargs['instance']
            self.fields['person'].queryset = ContactPerson.objects.filter(centre=email.centre)

