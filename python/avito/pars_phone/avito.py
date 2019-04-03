from selenium import webdriver
from time import sleep
from PIL import Image
from pytesseract import image_to_string

class Bot:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.navigate()

    def take_screenshot(self):
        self.driver.save_screenshot('screenshot.png')

    def tel_recon(self):
        image = Image.open('tel.gif')
        print(image_to_string(image))

    def crop(self, location, size):
        image = Image.open('screenshot.png')
        x = location['x']
        y = location['y']
        width = size['width']
        height = size['height']

        image.crop((x, y, x+width, y+height)).save('tel.gif')
        self.tel_recon()

    def navigate(self):
        self.driver.get('https://www.avito.ru/moskva/avtomobili/mercedes-benz_e-klass_2011_1407288202')

        button = self.driver.find_element_by_xpath('//button[@class="tooltip-button-3_N8y button-root-1vr-3 width-width-12-26fjt button-has_width-2tzgp button-root_size-m-2QhUm button-root_design-primary-27s3g"]')
        button.click()

        span = self.driver.find_element_by_xpath('//span[@class="item-phone-button-sub-text"]')
        span.click()

        sleep(3)

        self.take_screenshot()

        image = self.driver.find_element_by_xpath('//div[@class="item-phone-big-number js-item-phone-big-number"]//*')
        location = image.location       #dict {'x': 2343, 'y': 23423}
        size = image.size               #dict {'width': 234, 'height': 234}

        self.crop(location, size)
        self.driver.quit()

def main():
    b = Bot()

if __name__ == '__main__':
    main()
