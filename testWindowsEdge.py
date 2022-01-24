from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
desired_cap = {
 'os_version': '11',
 'resolution': '1280x1024',
 'browser': 'Edge',
 'browser_version': 'latest',
 'os': 'Windows',
 'name': 'Kai Windows Test', # test name
 'build': 'Windows Test Job' # CI/CD job or build name
}
driver = webdriver.Remote(
    command_executor='https://kaiwei_a9ewDd:MU9DK7auHeJgzUhkSdBx@hub-cloud.browserstack.com/wd/hub',
    desired_capabilities=desired_cap)
try:
    driver.get("https://bstackdemo.com/")
    WebDriverWait(driver, 10).until(EC.title_contains("StackDemo"))

    try:
        assert "StackDemo" in driver.title
    except AssertionError:
        print('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"assertion failure", "reason": "Page title wrong"}}')

    # Get text of a product - iPhone 12
    item_on_page =  WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="1"]/p'))).text

    try:
        assert "iPhone 11" in item_on_page
    except AssertionError:
        print('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"assertion failure", "reason": "1st item not iPhone 12"}}')


    # Click the 'Add to cart' button if it is visible
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="2"]/div[4]'))).click()
    # Check if the Cart pane is visible
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME, "float-cart__content")))
    ## Get text of product in cart
    item_in_cart = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[2]/div[2]/div/div[3]/p[1]'))).text
    # Verify whether the product (iPhone 12) is added to cart

    try:
        assert item_in_cart in item_on_page
    except AssertionError:
        print('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"assertion failure", "reason": "iPhone 12 hasn\'t been successfully added to the cart!"}}')

    
    if item_on_page == item_in_cart:
        # Set the status of test as 'passed' or 'failed' based on the condition; if item is added to cart
        print('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "iPhone 12 has been successfully added to the cart!"}}')

except NoSuchElementException:
    print('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Some elements failed to load"}}')
# Stop the driver
driver.quit() 