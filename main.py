'''
    File name: scraper.py
    Author: Sascha Villing
    Date created: 12/8/2022
    Python Version: 2.7
'''
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common import desired_capabilities
import os
from src.scraper import get_events_for_city
from src.db_service import DBService
from dotenv import load_dotenv
import locale

if __name__ == "__main__":

    # Set locale for event time scraping
    locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')

    # Load environment variables
    load_dotenv()
    aws_key = os.environ.get('AWS_ACCESS_KEY')
    aws_secret = os.environ.get('AWS_SECRET')
    google_events_url = os.environ.get('GOOGLE_EVENTS_URL')
    cities = os.environ.get('CITIES').split(',')

    # DB Service
    db_service = DBService(aws_key, aws_secret)

    # Chrome Driver
    if False:
        # Local
        from webdriver_manager.chrome import ChromeDriverManager
        driver = webdriver.Chrome(ChromeDriverManager().install())
    else:
        # Docker
        driver = webdriver.Remote(
            command_executor='http://chrome:4444/wd/hub',
            desired_capabilities=desired_capabilities.DesiredCapabilities.CHROME
        )
    
    # Get events for cities
    print(cities)
    for city in cities:
        events = get_events_for_city(driver, google_events_url, city)
        for event in events:
            event.pretty_print()
            db_service.upload(event)
    
    driver.close()