import time
from pages.Funciones import Funciones_epidata
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from behave import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.common.by  import By
from pages.ActionUi import ActionUI
from pages.Navegador import Funciones_driver
from configuration.config import Datatest
import unittest


class ElementClick():
    def __init__(self, driver):
        self.driver = driver

    def Tiempo(self, tie):
        t = time.sleep(tie)
        return t

    def Texto_x_xpath(self,selector, texto):
        WebDriverWait(self.driver, timeout=5).until(
            EC.element_to_be_clickable(
                (By.XPATH,
                 selector))
        ).send_keys(texto)

    def Texto_x_css(self, selector, texto):
        WebDriverWait(self.driver, timeout=5).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR,
                 selector))
        ).send_keys(texto)

    def Click_x_css(self, selector, tiempo):
        WebDriverWait(self.driver, timeout=5).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR,
                 selector))
        ).click()

    def Click_x_Xpath(self, selector):
        WebDriverWait(self.driver, timeout=5).until(
            EC.element_to_be_clickable(
                (By.XPATH,
                 selector))
        ).click()


