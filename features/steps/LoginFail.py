import time
import pytest
from behave import *
from selenium import webdriver
import pages.ElementosPage
from configuration.config import Datatest
from pages.ElementosPage import ElementsPage
from pages.Navegador import Funciones_driver
from pages.Funciones import Funciones_epidata
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from pages.ActionUi import ActionUI


t = 0.2


@when(u'Escribiendo Cuit "{cuit}"')
def EscribiendoCuit(context, cuit):
    try:
        ElementsPage.Inputcuit(context, cuit)
    except:
        context.driver.close()
        assert False, "La prueba fallo en : Escribiendo Cuit '{cuit}'"


@when(u'Escribiendo password "{password}"')
def EscribiendoPassword(context, password):
    try:
        ElementsPage.Inputpassword(context, password)
    except:
        context.driver.close()
        assert False, "La prueba fallo en : Escribiendo Cuit '{password}'"


@when(u'Click en boton ingresar')
def BotonIngresar(context):
    try:
        ElementsPage.ClickIngresar(context)
        time.sleep(1)
    except:
        context.driver.close()
        assert False, "La prueba fallo en : Escribiendo nombre '{Nombre}' y '{Apellido}'"


@when(u' Validar Pop up credenciales incorrectas')
def ValidarPopUp(context):
    try:
        ElementsPage.ClickPopup(context)
    except:
        context.driver.close()
        assert False, "La prueba fallo en :Validar Pop up credenciales incorrectas"
    context.driver.close()

