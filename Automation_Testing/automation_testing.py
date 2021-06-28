# We can use the selenium package for Testing automation.
# http://allselenium.info/python-selenium-commands-cheat-sheet-frequently-used/
# https://www.seleniumeasy.com/test/


from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver.exe')

chrome_browser.get(
    'https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert "Selenium Easy Demo - Simple Form to Automate using Selenium" in chrome_browser.title

chrome_browser.quit()
