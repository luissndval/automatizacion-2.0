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


@given(u'Iniciando navegador')
def InicioNavegador(context):
    ElementsPage.OpenBrowser(context)
    global Fun
    Fun = Funciones_epidata(context.driver)
