from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Configuramos el perfil de Firefox para que no abra la ventana de diálogo de descarga
firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference("browser.download.folderList", 2)
firefox_profile.set_preference("browser.download.manager.showWhenStarting", False)
firefox_profile.set_preference("browser.download.dir", "/path/to/download/directory")
firefox_profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")

# Creamos una instancia del navegador Firefox con el perfil configurado
driver = webdriver.Firefox(firefox_profile=firefox_profile)

# Abrimos la página de inicio de sesión
driver.get("http://catalogo.imicar.cl/")

# Esperamos a que la página se cargue completamente
driver.implicitly_wait(10)

# Introducimos el nombre de usuario y la contraseña
username_field = driver.find_element_by_name("username")
password_field = driver.find_element_by_name("password")
username_field.send_keys("omora@imicar.cl")
password_field.send_keys("inicio01")
password_field.send_keys(Keys.RETURN)

# Esperamos a que se cargue la página del perfil
driver.implicitly_wait(10)

# Cerramos el navegador
driver.quit()
