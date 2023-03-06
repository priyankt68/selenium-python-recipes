def zoom_in_out():
    from selenium import webdriver
    import time

    driver = webdriver.Chrome()
    driver.get("https://www.lambdatest.com/")

    # zooming to 200%
    driver.execute_script("document.body.style['-webkit-transform'] = 'scale(2.0)';")
    time.sleep(1)

    # zoom in to 150%
    driver.execute_script("document.body.style['-webkit-transform'] = 'scale(1.5)';")
    time.sleep(1)

    # zoom in to 120%
    driver.execute_script("document.body.style['-webkit-transform'] = 'scale(1.2)';")
    time.sleep(1)

    # reset based to 100%
    driver.execute_script("document.body.style['-webkit-transform'] = 'scale(1.0)';")

    time.sleep(2)
    driver.quit()


if __name__ == '__main__':
    zoom_in_out()
