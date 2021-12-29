"""
作者：Coco
日期：2021年10月25日
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
driver = webdriver.Chrome(chrome_options=options, executable_path="C:/Users/Coco/Desktop/deiver/chromedriver.exe")
driver.get('www.baidu.com')
