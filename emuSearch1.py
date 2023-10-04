import credentials1
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import random
import string

mobile_emulation = {
    "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1652805818&rver=7.0.6738.0&wp=MBI_SSL&wreply=https:%2F%2Faccount.microsoft.com%2Fauth%2Fcomplete-signin%3Fru%3Dhttps%253A%252F%252Faccount.microsoft.com%252F%253Frefp%253Dsignedout-index%2526refd%253Dwww.bing.com&lc=1033&id=292666&lw=1&fl=easi2')

email = driver.find_element(by='xpath', value='//*[@id="i0116"]')
email.send_keys(credentials1.username)

time.sleep(0.5)
next = driver.find_element(by='xpath', value='//*[@id="idSIButton9"]')
next.click()

time.sleep(1)

nextpass = driver.find_element(by='xpath', value='//*[@id="i0118"]')
nextpass.send_keys(credentials1.password)
time.sleep(0.5)
signin = driver.find_element(by='xpath', value='//*[@id="idSIButton9"]')
signin.click()
time.sleep(0.5)
confsignin = driver.find_element(by='xpath', value='//*[@id="idSIButton9"]')
confsignin.click()

time.sleep(5)

driver.get('https://www.bing.com/')
time.sleep(0.5)
for x in range(35):
    randa = random.choice(string.ascii_letters)
    randb = random.choice(string.ascii_letters)
    randc = random.choice(string.ascii_letters)
    rand = str(f'{randa}{randb}{randc}')

    search = driver.find_element(by='xpath', value='//*[@id="sb_form_q"]')
    search.clear()
    search.send_keys(rand)
    time.sleep(0.5)
    enter = driver.find_element(by='xpath', value='//*[@id="sb_form_q"]')
    enter.submit()
    time.sleep(0.5)
driver.quit()