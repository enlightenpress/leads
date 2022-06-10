from pydoc import describe
from django.core.management.base import BaseCommand, CommandError
from scrapers.models import ScrapeQueue, Scraper
from leads.models import *

import logging

SCRAPERS = [
    {
        'name': 'osmgeocode',
        'source': 'OpenStreetMaps',
        'documentaion': 'Uses Nominatum API to gather geocoding data for addresses.'
    }, 
    {
        'name': 'OFSTED',
        'source': 'OFSTED',
        'documentaion': 'Web scraper for checking exsisting database entries against the OFSTED site.'
    }, 
    ]

class Command(BaseCommand):
    help='Initialise data for the scrapers.'

    def handle(self, *args, **options):
        logger = logging.getLogger('scraper')

        #Check the type of scraper and execute the approriate function
        for scraper in SCRAPERS:
            if Scraper.objects.filter(name=scraper['name']).all():
                continue
            try:
                source = DataSource.objects.get(source=scraper['source'])
            except:
                source = None

            if source is None:
                source = DataSource.objects.create(source=scraper['source'], description='')
                source.save()
                
            Scraper.objects.create(name=scraper['name'], datasource=source, documentation=scraper['documentaion'])
        