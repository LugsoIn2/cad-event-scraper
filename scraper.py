from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common import desired_capabilities

def get_events_for_city(driver, city):
    driver.get('https://www.bodenseeforum-konstanz.de/veranstaltungskalender/')
    eventTitles = driver.find_elements("xpath", "//div[contains(@class, 'eventon_list_event')]/p/a/span/span[contains(@class, 'evoet_title')]")
    for event in eventTitles:
        if event.text:
            print('Title3: ', event.text)

if __name__ == "__main__":
    driver = webdriver.Remote(
        command_executor='http://chrome:4444/wd/hub',
        desired_capabilities=desired_capabilities.DesiredCapabilities.CHROME
    )
    get_events_for_city(driver, 'Konstanz')
    driver.close()