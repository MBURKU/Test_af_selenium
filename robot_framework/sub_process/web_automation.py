"""This is web automation"""
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


class BrowserAutomation:
    """
    A class for automating web browsers using Selenium WebDriver.

    This class supports the initialization of a web browser session, navigating to URLs,
    and performing custom tasks within the browser. It is designed to be flexible and
    can be extended to support additional browser types and configurations.

    Attributes:
        browser_type (str): The type of browser to initialize. Currently supports 'Chrome'.
        driver (webdriver): The WebDriver instance for browser interactions.
    """

    def __init__(self, browser_type='Chrome'):
        """
        Initializes the BrowserAutomation class with the specified browser type.

        Sets up a WebDriver based on the specified browser type with custom options
        to minimize detectability and maximize functionality.

        Args:
            browser_type (str): The type of browser to use. Default is 'Chrome'.
        """
        self.browser_type = browser_type
        self.driver = self._init_driver()

    def _init_driver(self):
        """
        Private method to initialize a Selenium WebDriver with specific options.

        Configures the WebDriver to start maximized, in incognito mode, and with features
        that reduce its detectability by websites.

        Returns:
            webdriver.Chrome: A configured WebDriver instance.

        Raises:
            ValueError: If the specified browser type is unsupported.
        """
        chrome_options = Options()
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--incognito")

        if self.browser_type == 'Chrome':
            chromedriver_path = os.getenv('ChromeDriver')
            service = Service(executable_path=chromedriver_path)
            driver = webdriver.Chrome(service=service, options=chrome_options)
        else:
            raise ValueError("Unsupported browser type provided")
        return driver

    def open_url(self, url):
        """
        Navigate the WebDriver to a specified URL.

        Args:
            url (str): The URL to open in the browser.
        """
        self.driver.get(url)

    def close_browser(self):
        """
        Close the browser and quit the WebDriver session.

        Properly shuts down the browser and cleans up the WebDriver instance.
        """
        self.driver.quit()

    def perform_task(self, task_func, *args, **kwargs):
        """
        Perform a specific task function using the current WebDriver session.

        Allows for custom tasks to be executed within the browser session. The task
        function should accept a WebDriver instance as its first argument.

        Args:
            task_func (callable): The function to execute.
            *args: Variable length argument list for the task function.
            *kwargs: Arbitrary keyword arguments for the task function.

        Returns:
            Any: The return value from the task function.
        """
        return task_func(self.driver, *args, **kwargs)

    def wait(self, timer: int):
        """test"""
        time.sleep(timer)
