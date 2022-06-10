from audioop import add
import scrapy
import logging

from scrapyleads.items import Centre, Address, ContactPerson

# logging.basicConfig(
#     filename='\Users\jdtbo\Documents\Code\EPLeadManager\epleads\scrapyleads\scrapyleads.log',
#     filemode='a',
#     format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s'
#     datefmt='%H:%M:%S',
#     level=logging.DEBUG
# )


class DaynurseriesSpider(scrapy.Spider):
    name = 'daynurseries'
    allowed_domains = ['daynurseries.co.uk']
    start_urls = ['http://daynurseries.co.uk/day_nursery_search_results.cfm/searchcountry/England/startpage/1']

    def parse(self, response):
        for searchresult in response.css('div.search-result'):
            # yield {
            #     'name': searchresult.css('a.search-result-name::text').get().strip(),
            #     'address': searchresult.css('p.search-result-address::text').get(),
            # }
            
            centrepage = searchresult.css('a.search-result-name::attr(href)').get()
            if centrepage is not None:
                yield response.follow(centrepage, callback=self.parse_centre)

        # next = response.css('ul.pagination li')[-1]
        # if next.css('a::text').get().strip() == 'Next':
        #     yield response.follow(next.css('a.attr(href)'), self.parse)

    def parse_centre(self, response):
        centre = Centre()
        address = Address()
        centre['name'] = response.css('div.profile-header-left h1::text').get().strip()
        
        addressfields = response.css('div.profile-header-address span::text').getall()
        if addressfields[-1] == 'Submit a Review':
            addressfields.pop()
        
        if len(addressfields) >= 3:
            address['postcode'] = addressfields.pop()
            address['city'] = addressfields.pop()
            address['address_lines'] = ", ".join(addressfields)
            
        for profilecontent in response.css('div.profile-row-content ul'):
            heading = profilecontent.css('div.h4::text').get()
            if heading is None:
                continue

            #handle extract group/owner
            if heading == 'Group/Owner':
                group = profilecontent.css('li a::text').get()
                if group is not None:
                    centre['group'] = group
                else:
                    centre['group'] = ''

            #handle select person in charge
            if heading == 'Person in charge':
                persons = []
                primary_contact = True
                for p in profilecontent.css('li::text').getall():
                    if p is not None and p != heading:
                        person = ContactPerson()
                        p_details = p.split('(')
                        person['name'] = p_details[0]

                        if len(p_details) > 1:
                            person['position'] = p_details[1].replace(')', '')

                        person['primary_contact'] = primary_contact
                        persons.append(person)
                        primary_contact = False
                centre['persons'] = persons

            #handle extract local authority
            if heading == 'Local Authority / Social Services':
                la = profilecontent.css('li::text').get()
                if la is not None:
                    la = la.split('(')[0]
                    la.replace('City Council', '')
                    la.replace('County Council', '')
                    
                    address['district'] = la
                else: 
                    address['district'] = '' 

            #handle extract opening days
            if heading == 'Opening Days':
                days = profilecontent.css('li::text').get()
                if days is not None:
                    centre['opening_days'] = days

            #handle extract opening hours
            if heading == 'Opening Hours':
                hours = profilecontent.css('li::text').get()
                if hours is not None:
                    centre['opening_hours'] = hours
        
        centre['address'] = address
        
        return centre

            
