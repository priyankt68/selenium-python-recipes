
from PIL import Image
import os

images = ["https://priyanktrivedi.org/images/priyank4xx.jpg", "https://cdn.pixabay.com/photo/2020/02/06/09/39/summer-4823612_960_720.jpg"]


# time to wait 
intial_delay=4

def get_images(urls):

    # Open the url image, set stream to True, this will return the stream content.
    
    import shutil

    import requests
    files = []
    for url in urls:
        filename = url.split("/")[-1]


        # Open the url image, set stream to True, this will return the stream content.
        r = requests.get(url, stream = True)

        # Check if the image was retrieved successfully
        if r.status_code == 200:
            # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
            r.raw.decode_content = True
            
            # Open a local file with wb ( write binary ) permission.
            with open(filename,'wb') as f:
                shutil.copyfileobj(r.raw, f)
        abs_filepath = os.path.abspath(filename)
        files.append(abs_filepath)
    
    return files


def whatsapp_web():
    from selenium import webdriver
    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.action_chains import ActionChains
    driver = webdriver.Chrome()

    driver.get("https://web.whatsapp.com/")

    # Download images and get their absolute paths stored here.
    images_list = get_images(images)

    # Contact name to send images
    name = "Mom"

    input('Enter anything after scanning QR code')
    time.sleep(intial_delay)
    
    user = driver.find_element(By.XPATH, '//span[@title = "{}"]'.format(name))
    user.click()

    # Send images one by one.
    for image in images_list:
        print("Sending image {}".format(image))

        # Clicking on the "plus" button for attachment of any file.
        attachment_box = driver.find_element(By.XPATH,'//div[@title = "Attach"]')
        attachment_box.click()

        time.sleep(3)

        # Selecting the file.
        image_box = driver.find_element(By.XPATH,
        '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
        image_box.send_keys(image)

        time.sleep(2)

        # Clicking the green send button.
        send_button = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
        send_button.click()

        # allow sometime for sending this message. 
        # NOTE - Tweak this time based on the network speed.
        time.sleep(5)

    # can remove this if need to exit the driver immediately.
    time.sleep(1000)

    driver.quit()


if __name__ == '__main__':
    get_images(images)
    whatsapp_web()
