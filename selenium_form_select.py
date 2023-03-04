def search_website():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import selenium.common.exceptions
    import time
    from selenium.webdriver.support.select import Select
    driver = webdriver.Chrome()

    driver.get("https://lambdatest.com")

    try:
        select = Select(driver.find_element(By.ID, "test-select"))
    except selenium.common.exceptions.NoSuchElementException as e:
        raise Exception(e)
    else:
        # Selecting the second option in the dropdown
        select.select_by_index(1)

        # Selecting the option with text matching with :Screenshot
        select.select_by_visible_text("Screenshot")

        # Selecting the option with 'value' attribute equal to 'responsive'
        select.select_by_value("responsive")


    time.sleep(4)
    driver.quit()


if __name__ == '__main__':
    search_website()
