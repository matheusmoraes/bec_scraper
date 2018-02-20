from splinter import Browser
from log import log
from time import sleep

class Downloader():
    def __init__(self, browser=Browser('firefox')):
        self._browser = browser

    def visit(self, url):
        log.info('Visiting %s' % url)
        self._browser.visit(url)
        sleep(2)

    def click_by_xpath(self, selector):
        element = self._browser.find_by_xpath(selector)
        self.click(element)

    def click_element(self, element):
        clicked = False
        for i in range(0, 5):
            try:
                element.click()
                clicked = True
            except Exception:
                pass
        if not clicked:
            log.warning('ERROR: Failed to click element')
            raise ElementNotPresent


    def find_by_xpath(self, selector):
        for i in range(0, 5):
            if self._browser.is_element_present_by_xpath(selector, wait_time=1):
                return self._browser.find_by_xpath(selector)
        log.warning('Unable to find element with xpath %s' % selector)
        raise ElementNotPresent

    def get_html(self):
        return self._browser.html

    def quit(self):
        log.info('Quitting browser')
        self._browser.quit()


class ElementNotPresent(Exception):
    pass
