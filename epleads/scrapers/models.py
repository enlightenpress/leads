from django.db import models
from leads.models import DataSource, Centre

# Create your models here.
class Scraper(models.Model):
    name = models.CharField(max_length=100)
    datasource = models.ForeignKey(
        DataSource,
        on_delete=models.PROTECT,
        related_name='scrapers',
        related_query_name='scraper',
    )
    documentation = models.TextField()

    def __str__(self) -> str:
        return self.name

class ScrapeQueue(models.Model):
    HIGH = 'hi'
    MODERATE = 'mo'
    LOW = 'lo'

    PRIORITY_CHOICES = [
        (HIGH, 'High'),
        (MODERATE, 'Moderate'),
        (LOW, 'Low'),
    ]

    scraper = models.ForeignKey(
        Scraper,
        on_delete=models.CASCADE,
    )
    centre = models.ForeignKey(
        Centre,
        on_delete=models.CASCADE,
    )
    priority = models.CharField(
        max_length=2, 
        choices=PRIORITY_CHOICES
    )

    class Meta:
        unique_together=['scraper', 'centre']
    
    def __str__(self) -> str:
        return "%s - %s" % (self.centre, self.scraper)
