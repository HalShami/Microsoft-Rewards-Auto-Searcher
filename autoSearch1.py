import credentials1
import emuSearch1
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import random
import string

browser = webdriver.Chrome('C:\Program Files (x86)\chromedriver\chromedriver.exe')
browser.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1652805818&rver=7.0.6738.0&wp=MBI_SSL&wreply=https:%2F%2Faccount.microsoft.com%2Fauth%2Fcomplete-signin%3Fru%3Dhttps%253A%252F%252Faccount.microsoft.com%252F%253Frefp%253Dsignedout-index%2526refd%253Dwww.bing.com&lc=1033&id=292666&lw=1&fl=easi2')

email = browser.find_element(by='xpath', value='//*[@id="i0116"]')
email.send_keys(credentials1.username)

time.sleep(0.5)
next = browser.find_element(by='xpath', value='//*[@id="idSIButton9"]')
next.click()

time.sleep(1)

nextpass = browser.find_element(by='xpath', value='//*[@id="i0118"]')
nextpass.send_keys(credentials1.password)
time.sleep(0.5)
signin = browser.find_element(by='xpath', value='//*[@id="idSIButton9"]')
signin.click()
time.sleep(0.5)
confsignin = browser.find_element(by='xpath', value='//*[@id="idSIButton9"]')
confsignin.click()

time.sleep(5)

browser.get('https://www.bing.com/')
time.sleep(0.5)
for x in range(35):
    randa = random.choice(string.ascii_letters)
    randb = random.choice(string.ascii_letters)
    randc = random.choice(string.ascii_letters)
    rand = str(f'{randa}{randb}{randc}')

    search = browser.find_element(by='xpath', value='//*[@id="sb_form_q"]')
    search.clear()
    search.send_keys(rand)
    time.sleep(0.5)
    enter = browser.find_element(by='xpath', value='//*[@id="sb_form_q"]')
    enter.submit()
    time.sleep(0.5)



emuSearch1()