def cookie_manager():
    from selenium import webdriver
    import time

    driver = webdriver.Chrome()

    driver.get("https://www.lambdatest.com/")
    driver.add_cookie({"name": "user", "domain": "lambdatest.com", "value": "automation_user"})
    all_cookies = driver.get_cookies()
    for cookie in all_cookies:
        print(cookie)


    time.sleep(4)
    driver.quit()


if __name__ == '__main__':
    cookie_manager()
