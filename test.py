import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
chrome_driver_path = 'C:/temp/chromedriver.exe'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"webdriver.chrome.driver={chrome_driver_path}")
driver = webdriver.Chrome(options=chrome_options)
url = 'http://www.tongdocc.co.kr/'
driver.get(url)
xpath = "//h5[@class='golfu_btn']"
driver.find_element("xpath", xpath).click()
xpath = '//input[@type="text"]'
text = '01024465660'
driver.find_element("xpath", xpath).send_keys(text)
# xpath = '//input[@value="닫기"]'
