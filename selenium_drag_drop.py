def drag_and_drop():
    from selenium import webdriver
    import time

    # import Action chains
    from selenium.webdriver.common.action_chains import ActionChains

    driver = webdriver.Chrome()
    driver.get("https://www.lambdatest.com/")

    # create action chain object
    action = ActionChains(driver)

    time.sleep(2)
    driver.quit()


if __name__ == '__main__':
    drag_and_drop()
