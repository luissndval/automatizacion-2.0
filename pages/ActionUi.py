import time
import unittest
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by  import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from allure_behave.hooks import allure_report
import allure
from allure_commons.types import  AttachmentType
from selenium.common.exceptions import TimeoutException


class ActionUI():

    def __init__(self, driver):
        self.driver = driver
        global act
        act=ActionChains(self.driver)



    def Tiempo(self, tie):
        t = time.sleep(tie)
        return t

    def SEX(self,elemento):
        val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, elemento)))
        val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
        val = self.driver.find_element(By.XPATH,elemento)
        return val

    def SEI(self, elemento):
        val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, elemento)))
        val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
        val = self.driver.find_element(By.ID,elemento)
        return val

    def autocomplet(self,tipo,selector,texto,tiempo):
        if (tipo=="xpath"):
            try:
                val=self.SEX(selector)
                act.click(val).send_keys(texto).\
                    key_down(Keys.ARROW_DOWN).\
                    key_up(Keys.ARROW_DOWN).\
                    key_down(Keys.ENTER).\
                    key_up(Keys.ENTER).perform()
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t
        elif (tipo == "id"):
            try:
                val = self.SEI(selector)
                act.click(val).send_keys("english").perform()
                time.sleep(3)#send_keys(texto).key_down(Keys.ENTER).perform()
                act.key_down(Keys.ARROW_DOWN).\
                    key_up(Keys.ARROW_DOWN).\
                    key_down(Keys.ENTER).\
                    key_up(Keys.ENTER).perform()
                time.sleep(1)
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t

    def Selection(self, tipo, selector, tiempo):
        if (tipo == "xpath"):
            try:
                val = self.SEX(selector)
                act.click(val).perform()
                time.sleep(1)
                act.key_down(Keys.ARROW_DOWN).\
                    key_up(Keys.ARROW_DOWN).\
                    key_down(Keys.ENTER).\
                    key_up(Keys.ENTER).perform()
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t
        elif (tipo == "id"):
            try:
                val = self.SEI(selector)
                act.click(val).perform()
                time.sleep(1)
                act.key_down(Keys.ARROW_DOWN).\
                    key_up(Keys.ARROW_DOWN).\
                    key_down(Keys.ENTER).\
                    key_up(Keys.ENTER).perform()
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t
    def TextoAction(self, tipo, selector,texto,tiempo):
        if (tipo == "xpath"):
            try:
                val = self.SEX(selector)
                act.click(val).perform()
                act.send_keys(texto).perform()
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t
        elif (tipo == "id"):
            try:
                val = self.SEX(selector)
                act.click(val).send_keys(texto).perform()
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("\nNo se encontro el Elemento " + selector)
                return t

    def ClickAction(self, tipo, selector, tiempo):
        if (tipo == "xpath"):
            try:
                val = self.SEX(selector)
                act.click(val).perform()
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t
        elif (tipo == "id"):
            try:
                val = self.SEI(selector)
                act.click(val).perform()
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("\nNo se encontro el Elemento " + selector)
                return t







if __name__ == "__main__":
    import sys