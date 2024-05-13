"""This module contains the main process of the robot."""
from OpenOrchestrator.orchestrator_connection.connection import OrchestratorConnection
from selenium.webdriver.common.by import By
from robot_framework.sub_process.web_automation import BrowserAutomation


def process(orchestrator_connection: OrchestratorConnection) -> None:
    """Do the primary process of the robot."""
    orchestrator_connection.log_trace("Running process.")
    orchestrator_connection.log_trace("Test af selenium.")

    automation = BrowserAutomation()
    automation.open_url('http://www.dr.dk')

    def click_smt(driver):
        """test"""
        driver.find_element(By.CSS_SELECTOR, '#drCookieDialogBody > div > div > div.submitButtons > div > div:nth-child(2) > button').click()
        automation.wait(5)
        driver.find_element(By.CSS_SELECTOR, r'#hydra-urn\:dr\:drupal\:article\:36c8f71d-8a33-49a7-934d-55a472795b2d > div > div > div.dre-teaser-content > div > a > span > span').click()

    automation.perform_task(click_smt)
    automation.wait(10)
    automation.close_browser()
