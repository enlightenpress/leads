from django.core.management.base import BaseCommand, CommandError
from scrapers.models import ScrapeQueue, Scraper
from leads.models import *

import logging

class Command(BaseCommand):
    help='Scrapes the next centre using the specified scraper from the Scrape Queue'

    def handle(self, *args, **options):
        logger = logging.getLogger('scraper')
        scrape = ScrapeQueue.objects.first()
        if scrape is None:
            logger.info('No scrape jobs in queue')
            return
        logger.info('Starting scrape for %s using %s' % (scrape.centre, scrape.scraper))

        #Check the type of scraper and execute the approriate function
        if scrape.scraper.name == 'ofsted':
            return
        elif scrape.scraper.name == 'daynurseries':
            return
        else:
            logger.warning('No scraper defined for: %s', scrape.scraper)
        
        scrape.delete()