'''
    File name: scraper.py
    Get all events today
    Date created: 12/8/2022
    Python Version: 3.7
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
    cities = os.environ.get('CITIES')
    cmd_exec = os.environ.get('CMD_EXEC')
    ev_table_name = os.environ.get('EV_TABLE_NAME')
    ten_table_name = os.environ.get('TEN_TABLE_NAME')

    # DB Service
    db_service = DBService(aws_key, aws_secret, ev_table_name, ten_table_name)

    # Chrome Driver
    if False:
        # Local
        from webdriver_manager.chrome import ChromeDriverManager
        driver = webdriver.Chrome(ChromeDriverManager().install())
    else:
        # Docker
        driver = webdriver.Remote(
            command_executor=cmd_exec,
            desired_capabilities=desired_capabilities.DesiredCapabilities.CHROME
        )
    
    # If city environment var not set -> Get events for all free tenants in 'tenants' dynamo db
    if not cities:  
        cities = db_service.get_tenants_to_fetch()
        print(cities)
    else:
        cities = cities.split(',')

    # Get events for cities in .env file
    for city in cities:
        events = get_events_for_city(driver, google_events_url, city)
        for event in events:
            event.pretty_print()
            db_service.upload_to_event_table(event)

    driver.close()