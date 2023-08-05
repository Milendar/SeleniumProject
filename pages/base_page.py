class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = "http://selenium1py.pythonanywhere.com/"

    def open(self):
        self.browser.get(self.url)