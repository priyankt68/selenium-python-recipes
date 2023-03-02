def search_website():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time

    driver = webdriver.Chrome()

    driver.get("https://www.wikipedia.org/")

    element = driver.find_element(By.ID, 'searchInput')
    element.send_keys("Selenium Software")
    element.submit()

    time.sleep(5)
    driver.quit()


if __name__ == '__main__':
    search_website()
