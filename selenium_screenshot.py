import selenium


def take_screenshot():
    from selenium import webdriver
    from selenium.webdriver.common.by import By

    import time

    driver = webdriver.Chrome()

    driver.get("https://www.lambdatest.com/blog/best-test-automation-frameworks-2021")
    driver.save_screenshot("screenshot_lambdatest.png")

    try:
        element = driver.find_element(By.ID, 'content')
    except selenium.common.exceptions.NoSuchElementException as e:
        raise Exception(e)
    else:
        try:
            element.screenshot("blog_content.png")
        except IOError as ioerror:
            raise ioerror

    time.sleep(4)
    driver.quit()


if __name__ == '__main__':
    take_screenshot()
