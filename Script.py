import os, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options

# phantom mode
options = Options(); options.headless = True
chrome_browser = webdriver.Firefox(options=options, executable_path=r'path\to\driver')

# waiting for element tp be found
def wait_element(delay, xpath): WebDriverWait(chrome_browser, delay).until(EC.presence_of_element_located((By.XPATH, xpath)))

# clear terminal
def clear(): os.system('cls')

try:
    start = time.time()
    clear(); print('Processing... Please wait...')
    chrome_browser.get('https://hotline.ua/')
    wait_element(15, "//div//input[@id='doSearch']")
    chrome_browser.find_element_by_xpath("//input[@id='searchbox'][@data-default='... найти товар']").send_keys('iPhone 7')
    chrome_browser.find_element_by_xpath("//div//input[@id='doSearch']").click()
    wait_element(15, "//h1[contains(text(), 'По запросу')]")
    chrome_browser.find_element_by_xpath("//p[@class='h4']//a[@data-tracking-id='catalog-10']").click()
    finish = time.time()
    clear(); print(f'Finished successfully!\n\nTakes {finish-start}s')
    chrome_browser.quit()
except TimeoutException:
    clear(); print('Nothing found!\n\nTry again!')
