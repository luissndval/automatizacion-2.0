from pages.Funciones import Funciones_epidata
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from behave import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.common.by import By
from pages.ActionUi import ActionUI
from pages.Navegador import Funciones_driver
from configuration.config import Datatest
import unittest

t = 1


class ElementsPage(Funciones_epidata):

    Campocuit = "//input[@id='cuit']"
    Campocontraseña = "//input[@placeholder='contraseña']"
    Btningresar = "//button[@type='submit']"
    textABMorganismo = "//h2[contains(.,'ABM de Organismos')]"
    btnCerrarSesion = "//a[@aria-label='Cerrar sesión']"
    textErrorLogin = "//div[@class='toast-body'][contains(.,'Error')]"


    """Constructor of CarrersPage class"""

    def __init__(self, driver):
        super().__init__(driver)

    def OpenBrowser(self):
        global navegador, fun
        navegador = Funciones_driver
        navegador.driver_Firefox(self, "C:\drivers\geckodriver.exe")
        fun = Funciones_epidata(self.driver)
        fun.Navegar(Datatest.URL, t)

    def Inputcuit(self, cuit):
        fun.Texto_Mixto("xpath", "//input[@formcontrolname='cuit']", cuit, t)

    def Inputpassword(self, password):
        fun.Texto_Mixto("xpath", "//input[@placeholder='contraseña']", password, t)

    def ClickIngresar(self):
        fun.Click_x_Xpath("//button[text()='Ingresar']")

    def Validariniciosesion(self):
        fun.Existe("xpath", "//h2[contains(.,'ABM de Organismos')]", t)


    def ClickCerrarSesion(self):
        fun.Click_x_Xpath("//a[contains(@class,'list-group-item list-group-item-logout logout-sm')]")

    def ClickPopup(self):
        #fun.click_prueba(By.XPATH,"ngb-toast[role='alert']")
        #fun.click_prueba1(By.XPATH,"ngb-toast[role='alert']")
        #fun.click_prueba2(By.XPATH,"ngb-toast[role='alert']")
        #fun.click_prueba3(By.XPATH,"ngb-toast[role='alert']")
        fun.click_prueba4(By.XPATH,"ngb-toast[role='alert']")


        #wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "ngb-toast[role='alert']")))




