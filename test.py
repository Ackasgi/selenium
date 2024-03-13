from selenium.webdriver.common.by import By
from selenium import webdriver
import time
chrome_driver_path = 'C:/temp/chromedriver.exe'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"webdriver.chrome.driver={chrome_driver_path}")
driver = webdriver.Chrome(options=chrome_options)
url = 'http://www.tongdocc.co.kr/'
driver.get(url)
time.sleep(0.5)
xpath = '//input[@value="닫기"]'
driver.find_element("xpath", xpath).click()
xpath = '//li[@class="loginpop"]'
driver.find_element("xpath", xpath).click()
time.sleep(1)
xpath = 'li [@rel="tab2"]'
driver.find_element("xpath", xpath).click()
#xpath = '//input[@type="text"]'
#text = '01023602724'
#driver.find_element("xpath", xpath).send_keys(text)