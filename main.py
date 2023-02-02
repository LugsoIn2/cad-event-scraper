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
from src.call_scraper import get_events_for_city
from src.db_service import DBService
from dotenv import load_dotenv
import locale

if __name__ == "__main__":
    
    print("--- Start Scraping ---")

    # Set locale for event time scraping
    locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')

    # Load environment variables
    load_dotenv()
    aws_key = os.environ.get('AWS_ACCESS_KEY')
    aws_secret = os.environ.get('AWS_SECRET')
    events_url = os.environ.get('EVENTS_URL')
    cities = os.environ.get('CITIES')
    cmd_exec = os.environ.get('CMD_EXEC')
    ev_table_name = os.environ.get('EV_TABLE_NAME')
    ten_table_name = os.environ.get('TEN_TABLE_NAME')
    scraper_name = os.environ.get('SCRAPER_NAME')
    

    # DB Service
    db_service = DBService(aws_key, aws_secret, ev_table_name, ten_table_name)

    # If city environment var not set -> Get events for all free tenants in 'tenants' dynamo db
    if not cities or cities.lower() == "generic":
        if scraper_name.lower() == "google" or scraper_name == "":
            cities = db_service.get_tenants_to_fetch()
        else:
            print(scraper_name.lower())
            print("wrong scraper name for generic scraper")
            exit(1)
    else:
        cities = cities.split(',')

    # Get events for cities in .env file
    for city in cities:
        # Chrome Driver
        print(city)
        print("--- Open Driver Connection ---")

        if True:
            # Local
            from webdriver_manager.chrome import ChromeDriverManager
            driver = webdriver.Chrome(ChromeDriverManager().install())
        else:
            # Docker
            driver = webdriver.Remote(
                command_executor=cmd_exec,
                desired_capabilities=desired_capabilities.DesiredCapabilities.CHROME
            )

        print("--- Getting Events ---")

        events = get_events_for_city(driver, events_url, city, scraper_name)
        for event in events:
            event.pretty_print()
            db_service.upload_to_event_table(event)

        driver.quit()

