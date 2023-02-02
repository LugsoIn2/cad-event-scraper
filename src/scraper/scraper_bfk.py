from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import desired_capabilities
from time import sleep
from src.event import Event
from datetime import datetime

def call_scraper(driver, url, city):
    events = []
    # Call event url
    driver.get(url)
    sleep(3)

    eventContainers = driver.find_elements("xpath","//div[contains(@class, 'eventon_list_event')]")
    for eventContainer in eventContainers:
        try:
            titleContainer = eventContainer.find_element("xpath",".//span[contains(@class, 'evcal_event_subtitle')]")
            if titleContainer.text:
                # Title
                title = titleContainer.text
                # Date
                day = eventContainer.find_element("xpath",".//em[contains(@class, 'date')]").text
                month = eventContainer.find_element("xpath",".//em[contains(@class, 'month')]").text
                date = datetime.strptime(day + '.' + month + '.' + str(datetime.now().year), "%d.%b.%Y")

                # Timestring
                eventContainer.click()
                sleep(1)
                time_string = eventContainer.find_element("xpath",".//span[contains(@class, 'evo_eventcard_time_t')]").text

                # Create event
                new_event = Event(title, date, time_string, 'Bodenseeforum', 'Konstanz', '', tenant=city)
                events.append(new_event)
        except:
            continue

    # Return list of events
    return events