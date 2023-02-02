from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import desired_capabilities
from time import sleep
from src.event import Event
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

def call_scraper(driver, url, city):
    events = []
    # Call google event url
    events_url = url.replace('$city$', city)
    driver.get(events_url)

    # Accept cookies
    accept_button = driver.find_elements("xpath", "//button[@jsname='b3VHJd']")
    if len(accept_button):
        accept_button[0].click()
    sleep(3) #TODO: how to wait for button click here?

    # Filter for events today
    today_button = driver.find_element("xpath", "//div[@jsname='SJ2nIb']")
    if today_button.get_attribute('aria-pressed') == 'false':
        today_button.click()
        sleep(3)

    # Scroll to bottom
    scroll_container = driver.find_element("xpath", "//div[@jsname='rymPhb']")
    scroll_origin = ScrollOrigin.from_element(scroll_container)
    old_scroll_container_height = 0
    new_scroll_container_height = scroll_container.size['height']
    while old_scroll_container_height < new_scroll_container_height:
        ActionChains(driver)\
            .scroll_from_origin(scroll_origin, 0, new_scroll_container_height)\
            .perform()
        sleep(1)
        old_scroll_container_height = new_scroll_container_height
        new_scroll_container_height = scroll_container.size['height']

    # Get all events
    eventTitles = driver.find_elements("xpath","//li[contains(@class, 'tv5olb')]")
    for event in eventTitles:
        # Get title
        title = event.find_element("xpath",".//div[contains(@class, 'YOGjf')]")
        driver.execute_script("arguments[0].scrollIntoView();", title)
        if title and title.text:
            # Get date            
            day = event.find_element("xpath",".//div[contains(@class, 'UIaQzd')]")
            month = event.find_element("xpath",".//div[contains(@class, 'wsnHcb')]")
            if day.text and month.text:
                date = datetime.strptime(day.text + '.' + month.text + '.' + str(datetime.now().year), "%d.%b.%Y")

                # Get timestring, location, city
                infos = event.find_elements("xpath",".//div[contains(@class, 'cEZxRc')]")
                if infos:
                    time_string = infos[0].text
                    location = infos[1].text
                    eventCity = infos[2].text if infos[2].text else infos[1].text
                
                # Picture
                picture_div = event.find_element("xpath", ".//div[contains(@class, 'H3ReNc')]/g-img/img")
                picture_url = picture_div.get_attribute("src")
                
                # Create event
                new_event = Event(title.text, date, time_string, location, eventCity, picture_url, tenant=city)
                events.append(new_event)
    
    # Return list of events
    return events