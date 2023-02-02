from time import sleep
from src.event import Event
from datetime import datetime
from selenium.webdriver import ActionChains

def call_scraper(driver, url, city):
    events = []
    # Call event url
    driver.get(url)
    sleep(3)

    eventContainers = driver.find_elements("xpath","//li[contains(@class, 'yIpRkq')]")
    for eventContainer in eventContainers:
        title = eventContainer.find_element("xpath",".//a[contains(@class, 'DjQEyU')]").text
        # Date
        dateString = eventContainer.find_element("xpath",".//div[contains(@class, 'v2vbgt')]")
        day = dateString.text[5:7]
        month = dateString.text[9:12]

        date = datetime.strptime(day + '.' + month + '.' + str(datetime.now().year), "%d.%b.%Y")
        # Time String
        action = ActionChains(driver)
        action.move_to_element(eventContainer).perform()
        time_string = eventContainer.find_element("xpath",".//div[contains(@class, 'I_kVM1')]").text

        # Picture
        picture_div = eventContainer.find_element("xpath", ".//wow-image[contains(@class, 'L5u5gG')]/img")
        picture_url = picture_div.get_attribute("src")

        # Create event
        new_event = Event(title, date, time_string, 'Kulturladen', 'Konstanz', picture_url, tenant=city)
        events.append(new_event)

    # Return list of events
    return events