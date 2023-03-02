def open_website(url):
    from selenium import webdriver
    import time

    driver = webdriver.Chrome()

    driver.get(url)

    time.sleep(2)

    driver.quit()


if __name__ == '__main__':
    url = "https://www.lambdatest.com/"
    open_website(url)
