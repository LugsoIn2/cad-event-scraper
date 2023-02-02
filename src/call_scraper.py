import os
from src.scraper.scraper_kula import call_scraper as get_kula_events
from src.scraper.scraper_google import call_scraper as get_google_events
from src.scraper.scraper_bfk import call_scraper as get_bfk_events

GOOGLE_EVENTS_URL = os.environ.get('GOOGLE_EVENTS_URL')

def get_events_for_city(driver, url, city, scraper_name):
    if not scraper_name or scraper_name == "GOOGLE":
        # GOOGLE EVENTS
        return get_google_events(driver, url, city)
    elif scraper_name == "KULA":
        # KULTURLADEN EVENTS
        return get_kula_events(driver, url, city)
    elif scraper_name == "BFK":
        # BODENSEEFORUM EVENTS
        return get_bfk_events(driver, url, city)
    else:
        # FAIL
        print('please set correct scraper_name env variable')
    
