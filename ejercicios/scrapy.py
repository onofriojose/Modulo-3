from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from msedge.selenium_tools import Edge, EdgeOptions

# Opciones para el driver de Edge
options = EdgeOptions()
options.use_chromium = True

# Cargar el driver de Edge
driver = Edge(options=options)

# Ingresar a la página de inicio de sesión
driver.get("http://catalogo.imicar.cl/")

# Encontrar los campos de usuario y contraseña
username = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")

# Ingresar las credenciales
username.send_keys("omora@imicar.cl")
password.send_keys("inicio01")

# Encontrar el formulario de inicio de sesión y hacer submit
form = driver.find_element_by_css_selector("#formularioLogin")
form.submit()