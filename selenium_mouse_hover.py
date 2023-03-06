def mouse_hover():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time

    # import Action chains
    from selenium.webdriver.common.action_chains import ActionChains

    driver = webdriver.Chrome()
    driver.get("https://lambdatest.com")

    # create action chain object
    action = ActionChains(driver)

    time.sleep(2)

    element = driver.find_element(By.XPATH, "//div[@class='inline-block "
                                            "dropdown desktop:block "
                                            "resource-dropdown']")

    action.move_to_element(element).perform()

    time.sleep(2)
    driver.quit()


if __name__ == '__main__':
    mouse_hover()
