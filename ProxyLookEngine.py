#переписываю с оптимизацией на реквесты
#получается открывать браузер, тыкать элементы, но сам список не получается утянуть

#import requests
#import webbrowser
#import re
#from fake_useragent import UserAgent
#from bs4 import BeautifulSoup
#from selenium.webdriver import Chrome
import selenium
from selenium import webdriver
import time
#import random

urlfull = 'https://hidemy.name/ru/proxy-list/?maxtime=150&type=h#list'
url = 'https://hidemy.name/ru/proxy-list/'

driver = webdriver.Chrome()
print ('Try to fetch data...')
driver.get(url)

print (driver.page_source)

#print ('Creating a session...')
#s = requests.session()
#print ('Try to fetch data...')
#html = s.get (url)
#print (html)
#print ('Waiting...')
##time.sleep (7)
#print ('Try to fetch data...')
#htmp = s.get (url)
#print (html)