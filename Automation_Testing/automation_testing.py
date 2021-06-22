# We can use the selenium package for Testing automation.
from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver.exe')

print(chrome_browser)
