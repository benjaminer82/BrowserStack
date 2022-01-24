from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
desired_cap = {
 'browserName': 'Android',
 'device': 'Vivo Y50',
 'realMobile': 'true',
 'os_version': '10.0',
 'name': 'Kai Vivo Y50 Test', # test name
 'build': 'Vivo Y50 Test Job' # CI/CD job or build name
}
driver = webdriver.Remote(
    command_executor='https://kaiwei_a9ewDd:MU9DK7auHeJgzUhkSdBx@hub-cloud.browserstack.com/wd/hub',
    desired_capabilities=desired_cap)
try:
    driver.get("https://bstackdemo.com/")
    WebDriverWait(driver, 10).until(EC.title_contains("StackDemo"))

    # 1st assertion to test the title of the page
    try:
        assert "StackDemo" in driver.title
    except AssertionError:
        print('"status":"assertion failure", "reason": "Page title wrong"')

    item_on_page =  WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="1"]/p'))).text

    # 2nd assertion to test if the 1st item on the page is an iPhone 12 item
    try:
        assert "iPhone 12" in item_on_page
    except AssertionError:
        print('"status":"assertion failure", "reason": "1st item not iPhone 12"')

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="1"]/div[4]'))).click()
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME, "float-cart__content")))
    item_in_cart = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[2]/div[2]/div/div[3]/p[1]'))).text

    # 3rd assertion to test if the iPhone 12 item has been correctly added to the cart
    try:
        assert item_in_cart in item_on_page
    except AssertionError:
        print('"status":"assertion failure", "reason": "iPhone 12 hasn\'t been successfully added to the cart!"')

    
    if item_on_page == item_in_cart:
        driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "iPhone 12 has been successfully added to the cart!"}}')

except NoSuchElementException:
    print('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Some elements failed to load"}}')

driver.quit() 