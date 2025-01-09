from idlelib.editor import darwin

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.saucedemo.com/")
driver.maximize_window()

username_field = driver.find_element(By.XPATH, '//input[@id="user-name"]')
password_field = driver.find_element(By.XPATH, '//input[@id="password"]')
login_button =  driver.find_element(By.XPATH, '//input[@id="login-button"]')

login = "standard_user"
username_field.send_keys(login)

password = "secret_sauce"
password_field.send_keys(password)

login_button.click()

sleep(5)