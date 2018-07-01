from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
import time
import re

web='1234'

while True:
    host=input("Nhap Firewall ban muon vao view: ")
    find=re.compile(host)
    if (find.search(web)!=None):
        break;
    print("Ban nhap sai, vui long nhap dung theo mau")
host=int(host)

if host==1:
    ulr='https://www.facebook.com/login.php'
elif host==2:
    ulr='https://mail.viettel.com.vn/#1'
elif host==3:
    ulr='http://192.168.9.1/'
elif host==4:
    ulr='https://www.facebook.com/login.php'


driver = webdriver.Chrome("C:\\Users\\Administrator\\Desktop\\project\\login\\chromedriver_win32\\chromedriver.exe")
driver.get(ulr)
print("Opened facebook...")

email = driver.find_element_by_xpath("//input[@id='email' or @name='email' or @id='username' or @id='userName']")
email.send_keys('admin')

print("Email Id entered...")
password = driver.find_element_by_xpath("//input[@id='pass' or @id='password' or @id='pcPassword']")
password.send_keys('135792468')
print("Password entered...")

button = driver.find_element_by_xpath("//button[@id='loginbutton']")
button.click()
print("FB opened")