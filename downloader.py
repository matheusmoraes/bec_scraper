from splinter import Browser

class Downloader():
    def __init__(self, browser=Browser('chrome')):
        self._browser = browser

    def visit(self, url):
        self._browser.visit(url)

    def click_by_xpath(self, selector):
        element = self._browser.find_by_xpath(selector)
        self._click(element)

    def _click(self, element):
        element.click()

    def find_by_xpath(self, selector):
        return self._browser.find_by_xpath(selector)

    def get_html(self):
        return self._browser.html

    def quit(self):
        self._browser.quit()
