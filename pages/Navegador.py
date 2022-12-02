import time
import unittest
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium import webdriver
from selenium.webdriver.common.by  import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from allure_behave.hooks import allure_report
import warnings


class Funciones_driver():
    def __init__(self, driver):
        self.driver = driver

    def driver_Firefox(self, ruta) :#NAVEGADOR FIREFOX RUTA DEL DRIVE
        self.driver=(ruta)
        s=Service(ruta)
        self.driver=webdriver.Firefox(service=s)
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)


    def driver_Chrome(self,ruta):#NAVEGADOR FIREFOX RUTA DEL DRIVE
        self.driver=(ruta)
        s=Service(ruta)
        self.driver=webdriver.Chrome(service=s)
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

