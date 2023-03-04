def search_website():
    from selenium import webdriver
    import time

    driver = webdriver.Chrome()

    driver.get("https://lambdatest.com")
    driver.save_screenshot("screenshot_lambdatest.png")

    time.sleep(4)
    driver.quit()


if __name__ == '__main__':
    search_website()
