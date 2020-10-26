import os, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.firefox.options import Options

options = Options(); options.headless = False
chrome_browser = webdriver.Chrome(options=options, executable_path=r'C:\Users\Dark\Desktop\chromedriver.exe')
chrome_browser.maximize_window()

def wait_element(delay, xpath): WebDriverWait(chrome_browser, delay).until(EC.presence_of_element_located((By.XPATH, xpath)))
def clear(): os.system('cls')
def message(text): clear(); print(text); time.sleep(1)
def search_another(mes_text):
    while a == 1:
        clear(); again = input(mes_text + '\n')
        if again == 'y':
            clear(); req = input('Enter what to search:\n')
            if req == '': message('Input is empty!')
            else: return req
        elif again == 'n': message('Have a nice day!'); clear(); chrome_browser.quit(); exit()
        else: message('Wrong input!')

a = 1; request = 'iPhone 7'
while a == 1:
    try:
        clear(); print('Processing...')
        chrome_browser.get('https://hotline.ua/')
        wait_element(15, "//div//input[@id='doSearch']")
        chrome_browser.find_element_by_xpath("//input[@id='searchbox'][@data-default='... найти товар']").send_keys(request)
        chrome_browser.find_element_by_xpath("//div//input[@id='doSearch']").click()
        wait_element(15, "//h1[contains(text(), 'По запросу')]")
        chrome_browser.find_element_by_xpath("//p[@class='h4']//a[@data-tracking-id='catalog-10']").click()
        request = search_another('Product found!\n\nWant to search one more?')
    except TimeoutException: request = search_another('Nothing found! Try again?')
