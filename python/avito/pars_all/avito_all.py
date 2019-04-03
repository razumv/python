import requests
import csv
from bs4 import BeautifulSoup
from time import sleep
import urllib2
from selenium import webdriver
from PIL import Image
from pytesseract import image_to_string

def tel_recon(html):
    image = Image.open('tel.gif')
    print(image_to_string(image))
def crop(html, location, size):
    image = Image.open('screenshot.png')
    x = location['x']
    y = location['y']
    width = size['width']
    height = size['height']
    image.crop((x, y, x+width, y+height)).save('tel.gif')
    html.tel_recon()
def get_html(url):
    r = requests.get(url)
    return r.text
def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    pages = soup.find('div', class_='pagination-pages').find_all('a', class_='pagination-page')[-1].get('href')
    total_pages = pages.split('=')[1].split('&')[0]
    return int(total_pages)
def write_csv(data):
    with open('avito.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow( (data['seller'],
                          data['title'],
                          data['price'],
                          data['phone'],
                          data['url']) )
def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find('div', class_='catalog-main').find_all('div', class_='item_table')
    for ad in ads:
        try:
            title = ad.find('div', class_='description').find('h3').text.strip().decode('ascii')
        except:
            title = ''
        try:
            url = 'https://www.avito.ru' + ad.find('div', class_='description').find('h3').find('a').get('href')
        except:
            url = ''
        try:
            price = ad.find('div', class_='about').find('span', class_='price').text.strip().split("  ")[0]
        except:
            price = ''
        try:
            driver = webdriver.Firefox()
            driver.get(url)
            button = driver.find_element_by_xpath('//button[@class="tooltip-button-3_N8y button-root-1vr-3 width-width-12-26fjt button-has_width-2tzgp button-root_size-m-2QhUm button-root_design-primary-27s3g"]')
            button.click()
            span = driver.find_element_by_xpath('//span[@class="item-phone-button-sub-text"]')
            span.click()
            sleep(1)
            driver.save_screenshot('screenshot.png')
            image = driver.find_element_by_xpath('//div[@class="item-phone-big-number js-item-phone-big-number"]//*')
            location = image.location       #dict {'x': 2343, 'y': 23423}
            size = image.size               #dict {'width': 234, 'height': 234}
            image = Image.open('screenshot.png')
            x = location['x']
            y = location['y']
            width = size['width']
            height = size['height']
            image.crop((x, y, x+width, y+height)).save('tel.gif')
            driver.quit()
            img = Image.open('tel.gif')
            phone = image_to_string(img)
        except:
            phone = ''
        try:
            seller = driver.find_element_by_xpath('//div[@class="seller-info-value"]')
        except:
            seller = '' 
        data = {'title': title,
                'phone': phone,
                'price': price,
                'seller': seller,
                'url': url}
        print(data)
        write_csv(data)
def main():
    url = 'https://www.avito.ru/moskva/avtomobili?p=1'
    base_url = 'https://www.avito.ru/moskva/avtomobili?'
    page_part = 'p='
    query_part = '&pmin=1000000&radius=0'
    total_pages = get_total_pages(get_html(url))
    for i in range(1, total_pages):
        url_gen = base_url + page_part + str(i) + query_part
        html = get_html(url_gen)
        get_page_data(html)
        print(url_gen)
        sleep(0)
if __name__ == '__main__':
    main()