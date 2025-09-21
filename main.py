import os
import time

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By

def load_config():
    #确定路径
    config_path = 'config.yml'
    #确定文件存在
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"配置文件 {config_path} 不存在")
    #读取config
    with open(config_path, 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)
    return config

def from_config_get(config):
    #读取username, password
    if 'username' in config and 'password' in config:
        return config['username'], config['password']
    else :
        return None, None

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://172.20.3.81")
try:
    #判断是否已连接
    user_nameElement = driver.find_element(By.ID, "user_name")
    user_nameValue = user_nameElement.get_attribute("value")
    if user_nameValue[0] == ' ':
        config = load_config()
        username, password = from_config_get(config)
        if username != None and password != None:
            usernameElement = driver.find_element(By.ID, "username")
            usernameElement.clear()
            usernameElement.send_keys(username)
            usernamePassword = driver.find_element(By.ID, "password")
            usernamePassword.clear()
            usernamePassword.send_keys(password)
            chooseButton = driver.find_element(By.CSS_SELECTOR, "input[name='opt'][value='']")
            chooseButton.click()
            loginButton = driver.find_element(By.XPATH, "//input[@type='submit' and @value='登录' and contains(@class, 'bottom')]")
            loginButton.click()
    time.sleep(3)
except Exception as e:
    print("操作失败：", e)
finally:
    driver.quit()