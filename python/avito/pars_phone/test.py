# -*- coding:utf-8 -*-

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path="/home/chromedriver", chrome_options=options)
driver.get("https://www.avito.ru")
print(driver.page_source)
driver.quit()