# We can use the selenium package for Testing automation.
from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')
option.add_experimental_option("excludeSwitches", ['enable-automation'])

chrome_browser = webdriver.Chrome(
    chrome_options=option, executable_path='./chromedriver.exe')

url = 'https://www.google.com'

chrome_browser.get(url=url)

print(chrome_browser)
