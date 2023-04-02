# pip install Appium-Python-Client
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


# Configurando as capacidades do driver do Appium
@pytest.fixture(scope='function')
def appium_driver(request):
    capacidades = {
        'platformName': 'Android',
        'deviceName': 'emulator-5554',
        'appPackage': 'com.android.chrome',
        'appActivity': 'com.google.android.apps.chrome.Main',
        'noReset': True,
        'chromeOptions': {
            'args': [
                '--disable-fre',
                '--no-first-run',
                '--disable-default-apps',
                '--disable-extensions',
                '--no-default-browser-check',
                '--disable-infobars',
                '--disable-blink-features=AutomationControlled',
                '--disable-features=InfiniteSessionRestore'
            ],
            'prefs': {
                'profile.default_content_settings.popups': 0,
                'homepage': 'https://www.google.com/'
            }
        }
    }

    # Inicializando o driver do Appium
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capacidades)

    # Definindo a espera implícita
    driver.implicitly_wait(10)

    yield driver

    # Fechando o driver após cada teste
    driver.quit()


def test_validar_acesso_ao_site_com_sucesso(appium_driver):
    driver = appium_driver

    USERNAME_INPUT = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[1]/android.widget.EditText"
    PASSWORD_INPUT = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText"
    LOGIN_BUTTON = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.Button"
    TEXT_PRODUCTS = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]/android.view.View[4]"

    # Navegar até a página inicial do site
    driver.get('https://www.saucedemo.com/')
    time.sleep(5)

    # Preenchendo os campos de usuário e senha
    user_name = driver.find_element(AppiumBy.XPATH, USERNAME_INPUT)
    user_name.send_keys('standard_user')

    password = driver.find_element(AppiumBy.XPATH, PASSWORD_INPUT)
    password.send_keys('secret_sauce')

    # Clicando no botão de login
    login_button = driver.find_element(by=AppiumBy.XPATH, value= LOGIN_BUTTON)
    login_button.click()

    # Encontre o elemento pelo xpath para validação
    element = driver.find_element(AppiumBy.XPATH,TEXT_PRODUCTS)

    # Obtenha o texto do elemento
    element_text = element.text

    # Verifique se o texto "Products" existe no elemento
    assert "Products" in element_text



