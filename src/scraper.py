from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common import desired_capabilities
from time import sleep
from src.event import Event
import os
from datetime import datetime
import locale
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

def get_events_for_city(driver, url, city):
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

        date = datetime.strptime(day + '.' + month + '.' + str(datetime.now().year), "%d.%b.%Y").isoformat()
        # Time String
        time_string = eventContainer.find_element("xpath",".//div[contains(@class, 'MizEne')]").text

        # Picture
        picture_div = eventContainer.find_element("xpath", ".//wow-image[contains(@class, 'L5u5gG')]/img")
        picture_url = picture_div.get_attribute("src")

        # Create event
        new_event = Event(title, date, time_string, 'Kula Konstanz', 'Konstanz', picture_url, tenant=city)
        events.append(new_event)

    # Return list of events
    return events