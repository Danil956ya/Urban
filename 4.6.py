from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

def test_login_redirect():
    correct_url = 'https://www.saucedemo.com/inventory.html'
    get_url = driver.current_url
    assert correct_url == get_url, "Не прошли на страничку"

option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True) #Не закрывает браузер после теста.
# option.add_argument("--headless")
driver = webdriver.Chrome(options=option)
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

test_login_redirect()
