import selenium.common.exceptions


def search_website():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import selenium.common.exceptions
    import time
    driver = webdriver.Chrome()

    driver.get("https://accounts.lambdatest.com/register")

    try:
        name = driver.find_element(By.XPATH, "//input[@id='name']")
        email = driver.find_element(By.XPATH, "//input[@id='email']")
        userpassword = driver.find_element(By.XPATH, "//input[@id='userpassword']")
        phone = driver.find_element(By.XPATH, "//input[@id='phone']")
    except selenium.common.exceptions.NoSuchElementException as e:
        raise Exception(e)
    else:
        name.send_keys("Selenium Software")
        email.send_keys("testuser@gmail.com")
        userpassword.send_keys("strongpassword123!@#")
        phone.send_keys("8347384828")

    # Get element for button
    try:
        submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    except selenium.common.exceptions.NoSuchElementException as e:
        raise e
    else:
        submit_button.submit()

    time.sleep(10)
    driver.quit()


if __name__ == '__main__':
    search_website()
