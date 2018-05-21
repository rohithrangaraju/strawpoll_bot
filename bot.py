from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#
# PROXY = "23.23.23.23:3128"
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--proxy-server=%s' % PROXY)
#
#
#
# chrome = webdriver.Chrome("C:/Users/HP PC/Downloads/chromedriver_win32/chromedriver.exe",chrome_options=chrome_options)
proxyList = open('proxies.txt', 'r').read().split('\n')
proxyList = proxyList[4:len(proxyList)-4]

for i in proxyList:
    try:
        a = i.split(' ')[0]
        PROXY = a
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=%s' % PROXY)
        chrome = webdriver.Chrome(
            chrome_options=chrome_options)
        # chrome.set_page_load_timeout(20)
        chrome.get("https://strawpoll.com/xy47y85y#.Wt8q4FIBFKc")
        chrome.execute_script("document.getElementById('check1').click()")
        chrome.find_element_by_css_selector(".action.wide").click()
        chrome.implicitly_wait(1)
        # chrome.close()
    except:
        chrome.close()
