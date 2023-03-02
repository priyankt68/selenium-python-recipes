
def search_website(url, search_string):
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time

    driver = webdriver.Chrome()

    driver.get(url)

    element = driver.find_element(By.NAME, 'q')
    element.send_keys(search_string)
    element.submit()

    time.sleep(5)
    driver.quit()

if __name__ == '__main__':
    url = "https://www.google.com/"
    search = "Lambdatest"
    search_website(url, search)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
