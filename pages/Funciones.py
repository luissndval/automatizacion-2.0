import time
import os
import unittest
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from allure_behave.hooks import allure_report
import allure
from allure_commons.types import  AttachmentType


class Funciones_epidata():
    def __init__(self, driver):
        self.driver = driver

    def Tiempo(self, tie):
        t = time.sleep(tie)
        return t

    def Navegar(self, Url, Tiempo):
        self.driver.get(Url)
        self.driver.maximize_window()
        print("Página abierta: " + str(Url))

        t = time.sleep(Tiempo)
        return t

    def SEX(self, elemento):
        val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, elemento)))
        val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
        val = self.driver.find_element(By.XPATH, elemento)
        return val

    def SEI(self, elemento):
        val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, elemento)))
        val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
        val = self.driver.find_element(By.ID, elemento)
        return val

    def SEC(self, elemento):
        val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, elemento)))
        val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
        val = WebDriverWait(self.driver, timeout=5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, elemento)))
        return val

    def Texto_x_css(self, selector, texto):
        WebDriverWait(self.driver, timeout=5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,selector))).send_keys(texto)

    def Click_x_css(self, selector):
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

    def Texto_Mixto(self, tipo, selector, texto, tiempo=.1):

        if (tipo == "xpath"):
            try:
                val = self.SEX(selector)
                val.clear()
                val.send_keys(texto)
                print("\nVALIDADO (Escribiendo en el campo {} el texto) -> {} ".format(selector, texto))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t
        elif (tipo == "id"):
            try:
                val = self.SEI(selector)
                val.clear()
                val.send_keys(texto)
                print("\nCAMPO VALIDADO -- Escribiendo en el campo {} el texto -> {} ".format(selector, texto))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("\nNo se encontro el Elemento " + selector)
                return t
        elif (tipo == "css"):
            try:
                val = self.SEC(selector)
                val.clear()
                val.send_keys(texto)
                print("\nCAMPO VALIDADO -- Escribiendo en el campo {} el texto -> {} ".format(selector, texto))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("\nNo se encontro el Elemento " + selector)
                return t

    def Click_Mixto(self, tipo, selector, tiempo=.1):
        if tipo == "xpath":
            try:
                val = self.SEX(selector)
                val.click()
                print("\nCAMPO VALIDADO  -- dando click en {} -> {} ".format(selector, selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("\nNo se encontro el Elemento" + selector)
                return t
        elif tipo == "id":
            try:
                val = self.SEI(selector)
                val.click()
                print("\nCAMPO VALIDADO -- dando click en {} -> {} ".format(selector, selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("\nNo se encontro el Elemento" + selector)
                return t
        elif tipo == "css":
            try:
                val = self.SEC(selector)
                val.clear()
                val.click()
                print("\nCAMPO VALIDADO -- dando click en {} -> {} ".format(selector, selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("\nNo se encontro el Elemento " + selector)
                return t

    def Salida(self):
        print("\nSe termina la prueba Exitosamente")

    def Select_Xpath_Type(self, xpath, tipo, dato, tiempo):
        try:
            val = self.SEX(xpath)
            val = Select(val)

            if tipo == "text":
                val.select_by_visible_text(dato)
            elif tipo == "index":
                val.select_by_index(dato)
            elif tipo == "value":
                val.select_by_value(dato)

            print("\nCAMPO VALIDADO --- El campo Seleccionado es {} ".format(dato))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("\nNo se encontro el Elemento" + xpath)
            return t

    def Select_ID_Type(self, id, tipo, dato, tiempo):
        try:
            val = self.SEI(dato)
            val = Select(val)

            if tipo == "text":
                val.select_by_visible_text(dato)
            elif tipo == "index":
                val.select_by_index(dato)
            elif tipo == "value":
                val.select_by_value(dato)

            print(" \nCAMPO VALIDADO --- El campo Seleccionado es {} ".format(dato))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("\nNo se encontro el Elemento" + id)
            return t

    def Select_css_type(self, css, tipo, dato, tiempo):
        try:
            val = self.SEC(dato)
            val = Select(val)

            if tipo == "text":
                val.select_by_visible_text(dato)
            elif tipo == "index":
                val.select_by_index(dato)
            elif tipo == "value":
                val.select_by_value(dato)

            print(" \nCAMPO VALIDADO --- El campo Seleccionado es {} ".format(dato))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("\nNo se encontro el Elemento" + css)
            return t


    def Upload_Xpath(self, xpath,ruta,tiempo):
        try:
            val=self.SEX(xpath)
            val.send_keys(ruta)

            print("\nCAMPO VALIDADO --- Se carga la imagen {} ".format(ruta))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("\nNo se encontro el Elemento" + xpath)
            return t

    def Upload_ID(self, id,ruta,t):
        try:
            val=self.SEI(ruta)
            val.send_keys(ruta)

            print("\nCAMPO VALIDADO --- Se carga la imagen {} ".format(ruta))
            t = time.sleep(t)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("\nNo se encontro el Elemento" + id)
            return t

    def Upload_css(self,css,ruta,t):
        try:
            val = self.SEC(ruta)
            val.send_keys(ruta)

            print("\nCAMPO VALIDADO --- Se carga la imagen {} ".format(ruta))
            t = time.sleep(t)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("\nNo se encontro el Elemento" + css)
            return t


    def Existe(self, tipo, selector, tiempo):
        if (tipo == "xpath"):
            try:
                val=self.SEX(selector)
                print("\nEl elemento  {} -> existe ".format(val))
                t = time.sleep(tiempo)
                return "Existe"
            except TimeoutException as ex:
                print(ex.msg)
                print("\nNo se encontro el Elemento" + selector)
                return "\nNo Existe"
        elif (tipo == "id"):
            try:
                val=self.SEI(selector)
                print("\nEl elemento  {} -> existe ".format(val))
                t = time.sleep(tiempo)
                return "\nExiste"
            except TimeoutException as ex:
                print(ex.msg)
                print("\nNo se encontro el Elemento" + selector)
                return "\nNo Existe"
        elif (tipo == "css"):
            try:
                val=self.SEC(selector)
                print("\nEl elemento  {} -> existe ".format(val))
                t = time.sleep(tiempo)
                return "\nExiste"
            except TimeoutException as ex:
                print(ex.msg)
                print("\nNo se encontro el Elemento" + selector)
                return "\nNo Existe"

    def verificador_elementos(self, selector):
        try:
            #element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(selector))
            element=WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, selector)))
            return element.is_displayed()
        except:
            return False

    def captura_pantalla(self,nombre):
        allure.attach(self.driver.get_screenshot_as_png(),name=nombre,attachment_type=AttachmentType.PNG,)

    def extractorTXT (self,tipo,selector,ruta,w,t):
        if tipo == "xpath":
            try:
                val = self.SEX(selector).text
                texto= open(ruta,w)
                texto.write(val)
                texto.close()
                print("\nVALIDADO ( texto Capturado) -> {} ".format(selector, ruta))
                t = time.sleep(t)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t
        elif tipo == "id":
            try:
                val = self.SEX(selector).text
                texto = open(ruta, w)
                texto.write(val)
                texto.close()
                print("\nVALIDADO ( texto Capturado) -> {} ".format(selector, ruta))
            except TimeoutException as ex:
                print(ex.msg)
                print("\nNo se encontro el Elemento " + selector)
                return t
        elif tipo == "css":
            try:
                val = self.SEC(selector).text
                texto = open(ruta, w)
                texto.write(val)
                texto.close()
                print("\nVALIDADO ( texto Capturado) -> {} ".format(selector, ruta))
            except TimeoutException as ex:
                print(ex.msg)
                print("\nNo se encontro el Elemento " + selector)
                return t

    def click_prueba(self,tipo,selector):
        elem=WebDriverWait(self.driver, 5)\
            .until(EC.invisibility_of_element_located
                           ((tipo,selector)))
        return elem.is_displayed

    def click_prueba1(self,tipo,selector):
        elem=WebDriverWait(self.driver, 5).until(EC.frame_to_be_available_and_switch_to_it(( tipo, selector)))
        return elem.is_displayed

    def click_prueba2(self,tipo,selector):
        elem= WebDriverWait(self.driver, 5).until(EC.invisibility_of_element(( tipo, selector)))
        return elem.is_displayed

    def click_prueba3(self,tipo,selector):
        elem= WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located(( tipo, selector)))
        return elem.is_displayed

    def click_prueba4(self,tipo,selector):
        elem= WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        return elem.is_displayed







