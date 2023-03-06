def drag_and_drop():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time

    # import Action chains
    from selenium.webdriver.common.action_chains import ActionChains

    driver = webdriver.Chrome()
    driver.get("https://www.lambdatest.com/")

    # create action chain object
    action = ActionChains(driver)

    time.sleep(2)
    # get element
    element = driver.find_element(By.LINK_TEXT, "Enterprise")
    # click on the link.
    action.click(on_element=element)

    # execute the action defined above
    action.perform()

    time.sleep(2)
    driver.quit()


if __name__ == '__main__':
    drag_and_drop()
