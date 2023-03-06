def drag_and_drop():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time

    # import Action chains
    from selenium.webdriver.common.action_chains import ActionChains

    driver = webdriver.Chrome()
    driver.get("https://www.w3schools.com/html/html5_draganddrop.asp")

    # create action chain object
    action = ActionChains(driver)

    time.sleep(2)

    source_element = driver.find_element(By.ID, "div1")
    target_element = driver.find_element(By.ID, "div2")
    action.drag_and_drop(source_element, target_element).perform()

    time.sleep(2)
    driver.quit()


if __name__ == '__main__':
    drag_and_drop()
