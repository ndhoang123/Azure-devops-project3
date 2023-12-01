# #!/usr/bin/env python
from asyncio import sleep
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

def getTimestamp():
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return (time + '\t')

# Start the browser and login with standard_user
def login (user, password):
    print (getTimestamp() + ': Starting the browser...')
    # --uncomment when running in Azure DevOps.
    options = ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--remote-debugging-port=9222")
    driver = webdriver.Chrome(options=options)
    url = 'https://www.saucedemo.com/'
    print (getTimestamp() + ': Browser started successfully. Navigating to the demo page to login.')

    driver.get(url)
    driver.find_element("css selector", "input[id='user-name']").send_keys(user)
    driver.find_element("css selector", "input[id='password']").send_keys(password)
    driver.find_element("css selector", "input[id='login-button']").click()
    
    sleep(10)
    ## Check if login succesfully or not
    title = driver.find_element("css selector", "span[class='title']").text
    assert "products" in title.lower()
    print(getTimestamp() + "TEST PASSED : LOGIN SUCCESSFUL")

    print(getTimestamp() + 'login username {:s} - password {:s} successfully'.format(user, password))
    print(getTimestamp() + driver.current_url)

    return driver

def GoToDetailPage(driver, items):
    print(getTimestamp() + 'Test: Go to detail page and add items')
    for i in range(items):
        element = "a[id='item_" + str(i) + "_title_link']"
        driver.find_element("css selector", element).click()
        driver.find_element("css selector", "button.btn_primary.btn_inventory").click()
        product = driver.find_element("css selector", '.inventory_details_name.large_size').text
        print(getTimestamp() + product + "added to cart")
        driver.find_element("css selector", "button.inventory_details_back_button").click()
    print(getTimestamp() + '{:d} items are all added to cart successfully'.format(items))

def RemoveItems(driver, items):
    print(getTimestamp() + 'Test: Delete items')
    for i in range(items):
        element = "a[id='item_" + str(i) + "_title_link']"
        driver.find_element("css selector", element).click()
        driver.find_element("css selector", "button.btn_secondary.btn_inventory").click()
        product = driver.find_element("css selector", '.inventory_details_name.large_size').text
        print(getTimestamp() + product + "removed from the cart")
        driver.find_element("css selector", "button.inventory_details_back_button").click()
    print(getTimestamp() + '{:d} items are all added to cart successfully'.format(items))

def GoToCartPage(driver):
    print(getTimestamp() + "Test: Go to CartPage")
    element = "a[class='shopping_cart_link']"
    driver.find_element("css selector", element).click()
    ## Check if going to the cart page or not
    title = driver.find_element("css selector", "span[class='title']").text
    assert "your cart" in title.lower()
    print(getTimestamp() + "TEST PASSED : Be at Cart page SUCCESSFUL")

def GoToCheckoutInfomationPage(driver):
    print(getTimestamp() + "Test: Go to Checkout information page")
    element = "button[id='checkout']"
    driver.find_element("css selector", element).click()
    ## Check if going to the cart page or not
    title = driver.find_element("css selector", "span[class='title']").text
    assert "checkout: your information" in title.lower()
    print(getTimestamp() + "TEST PASSED : Be at check out page SUCCESSFUL")

    first_name = "Andrea"
    last_name = "Nguyen"
    postal_code = "AB1212"
    driver.find_element("css selector", "input[id='first-name']").send_keys(first_name)
    driver.find_element("css selector", "input[id='last-name']").send_keys(last_name)
    driver.find_element("css selector", "input[id='postal-code']").send_keys(postal_code)
    driver.find_element("css selector", "input[id='continue']").click()

def GoToCheckoutOverviewPage(driver):
    title = driver.find_element("css selector", "span[class='title']").text
    assert "checkout: overview" in title.lower()
    print(getTimestamp() + "TEST PASSED : Be at cart overview page SUCCESSFUL")

def GoToFinishPage(driver):
    print(getTimestamp() + "Test: Go to finish page")
    element = "button[id='finish']"
    driver.find_element("css selector", element).click()
    # Check if be at checkout page or not
    title = driver.find_element("css selector", "span[class='title']").text
    assert "checkout: complete!" in title.lower()
    title = driver.find_element("css selector", "h2[class='complete-header']").text
    assert "thank you for your order!" in title.lower()

    element = "button[id='back-to-products']"
    driver.find_element("css selector", element).click()

if __name__ == "__main__":
    driver = login('standard_user', 'secret_sauce')
    GoToDetailPage(driver, 5)
    RemoveItems(driver, 5)
    GoToCartPage(driver)
    GoToCheckoutInfomationPage(driver)
    GoToCheckoutOverviewPage(driver)
    GoToFinishPage(driver)
