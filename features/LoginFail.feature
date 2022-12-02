Feature: Iniciar sesion con credenciales invalidas
  Background:
    Given Iniciando navegador

    Scenario Outline: Se visualiza campos para iniciar sesion
      When Escribiendo Cuit "<cuit>"
      When Escribiendo password "<password>"
      When Click en boton ingresar
      When Validar Pop up credenciales incorrectas


      Examples:
      |cuit|password|
      #Datos invalidos
      |23432002209|assdf|


