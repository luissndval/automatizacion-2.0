Feature: Iniciar sesion con credenciales validas
  Background:
    Given Iniciando navegador

    Scenario Outline: Se visualiza campos para iniciar sesion
      When Escribiendo Cuit "<cuit>"
      When Escribiendo password "<password>"
      Then Click en boton ingresar
      Then Click en cerrar sesion


      Examples:
      |cuit|password|
      # Datos validos
      |27395625123|Troquel1|
#      #Datos invalidos
#      |23432002209|assdf   |




