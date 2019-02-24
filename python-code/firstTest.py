#!/usr/bin/env python3

import datetime
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def execSearch(assignBrowser: webdriver):
    dateString = datetime.datetime.today().strftime("%Y%m%d%H%M%S")

    # Open the browser with assign URL
    assignBrowser.get('https://google.com')

    # Input keyword in search field
    search_box = assignBrowser.find_element_by_name("q")
    search_box.send_keys('WilliamTai.moe')

    # Submit search
    search_box.submit()

    # Take screenshot and save to local disk
    assignBrowser.save_screenshot('./tmp/selenium_screenshot/' + dateString + '.png')

if __name__ == '__main__':
    try:
        # Remote headless browser
        browser = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)

        # Run remote selenium browser
        execSearch(browser)
    
    except:
        print("Error occurt!")
        raise

    finally:
        # Close and quit the remote browser
        browser.close()
        browser.quit()
