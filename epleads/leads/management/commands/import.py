from django.core.management.base import BaseCommand, CommandError
from leads.resource import *
import tablib
import logging

logger = logging.getLogger('import_export')
    
def get_model_resource(model):
    if model  == 'centre':
        return CentreResource()
    if model == 'email':
        return EmailResource()
    if model == 'phone':
        return PhoneResource()
    if model == 'opening_hours':
        return OpeningHoursResource()
    if model == 'contact_person':
        return ContactPersonResource()
    if model == 'address':
        return AddressResource()
    
    return None

class Command(BaseCommand):
    help='Import data from a file. Using the format of the model resources specified. This assumes that the dataset has headers.'
    model_choices = ['centre', 'email', 'phone', 'opening_hours', 'contact_person', 'address']

    def add_arguments(self, parser) -> None:
        parser.add_argument('model', nargs='+', choices=self.model_choices)
        parser.add_argument('file', nargs='+', type=open)
    
    def handle(self, *args, **options):
        print(options['file'][0].name)
        imported_data = tablib.Dataset().load(options['file'][0])
        # print(imported_data)
        # with open(options['file'], 'r') as fh:
        #     imported_data = tablib.Dataset().load(fh)

        resource = get_model_resource(options['model'][0])
        print(resource)
        
        result = resource.import_data(imported_data, dry_run=True, raise_errors=True)
        print("Has validation errors? %s " % result.has_validation_errors())

        print(result)

        if not result.has_errors():
            result = resource.import_data(imported_data, dry_run=False)
            print("Success!")
            pass
        else:
            print("Fail!")
            logger.error("Errors occured when importing data for model %s from the file %s" % (options['model'][0], options['file'][0].name))
