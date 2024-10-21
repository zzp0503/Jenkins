from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()


def get(data):
    driver.get(data)


def maximize():
    driver.maximize_window()


def send_key(element, data, element_type=1, index=None):
    # type1代表使用element方法， type2代表使用elements方法。默认使用element方法。
    if element_type == 1:
        driver.find_element(By.XPATH, element).send_keys(data)
    elif element_type == 2:
        driver.find_elements(By.XPATH, element)[index].send_keys(data)


def chick(element, element_type=1, index=None):
    # type1代表使用element方法， type2代表使用elements方法。默认使用element方法。
    if element_type == 1:
        driver.find_element(By.XPATH, element).click()
    elif element_type == 2:
        driver.find_elements(By.XPATH, element)[index].click()


def script_chick(element, element_type=1, index=None):
    if element_type == 1:
        info = driver.find_element(By.XPATH, element)
        driver.execute_script("arguments[0].click();", info)
    elif element_type == 2:
        info = driver.find_elements(By.XPATH, element)
        driver.execute_script("arguments[0].click();", info)[index].click()


def text(element, element_type=1, index=None):
    if element_type == 1:
        msg = driver.find_element(By.XPATH, element).text
        return msg
    elif element_type == 2:
        msg = driver.find_elements(By.XPATH, element)[index].text
        return msg


def select_index(element, index):
    info = Select(driver.find_element(By.XPATH, element))
    info.select_by_index(index)


def implicitly_wait(time):
    driver.implicitly_wait(time)


def actions_Chains(actions_type, element):
    # actions_type=1 代表 使用悬停方法  actions_type=2 代表使用鼠标点击方法
    actions = ActionChains(driver)
    if actions_type == 1:
        a = driver.find_element(By.XPATH, element)
        actions.move_to_element(a).perform()
    if actions_type == 2:
        a = driver.find_element(By.XPATH, element)
        actions.click_and_hold(a).perform()


def close():
    driver.close()


def clear(element, element_type=1, index=None):
    if element_type == 1:
        driver.find_element(By.XPATH, element).clear()
    elif element_type == 2:
        driver.find_elements(By.XPATH, element)[index].clear()


def screenshot(title,path ):
    driver.get_screenshot_as_file(f"{path}/{title}.png")
