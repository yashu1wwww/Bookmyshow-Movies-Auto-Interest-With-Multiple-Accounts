from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time
import random

# List of email addresses change to your required..
email_list = [
    'mysy@gmail.com', 'myy@gmail.com', 'my@gmail.com', 'm.y@gmail.com', '.my@gmail.com', 
    'm.y@gmail.com', 'mygmail+marva@gmail.com', 'my@gmail.com', 'mygmail+derik@gmail.com', 
    'mygmail+alvie@gmail.com', 'my@gmail.com', 'mygmail+gage@gmail.com', 'mygmail+max@gmail.com', 
    'my@gmail.com', 'mygmail+lita@gmail.com', 'mygmail+ginny@gmail.com', 'mygmail+timmy@gmail.com', 
    'mygmail+kent@gmail.com', 'mygmail+kali@gmail.com', 'mygmail+bryce@gmail.com', 'my@gmail.com', 
    'mygmail+rosie@gmail.com', 'mygmail+madge@gmail.com', 'my@gmail.com', 'mygmail+keily@gmail.com', 
    'my@gmail.com', 'mygmail+evans@gmail.com', 'mygmail+stan@gmail.com', 'mygmail+kaye@gmail.com'
]

option = webdriver.ChromeOptions()
option.add_experimental_option("debuggerAddress", "localhost:9222")
driver = webdriver.Chrome(options=option)
driver.maximize_window()

def visit_bookmyshow():
    driver.get("https://in.bookmyshow.com") #change with required movie(auto interest button required movie) url....
    time.sleep(5)

def click_im_interested():
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/section[1]/div/div/div[2]/section/div[2]/div/button").click() #interest button click
    time.sleep(2)

def click_continue_with_email():
    driver.find_element(By.XPATH, '//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #click email option
    time.sleep(2)

def enter_email(email):
    email_input = driver.find_element(By.CSS_SELECTOR, '#emailId') #email select orderwise
    email_input.send_keys(email)
    time.sleep(1)
    email_input.send_keys(Keys.ENTER)

def confirm_interest():
    time.sleep(15)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/section[1]/div/div/div[2]/section/div[2]/div/button").click() #click on interest button
    time.sleep(2)

def sign_out():
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div[1]/div/div/div/div[2]/div[2]/span").click() #human logo
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout
    time.sleep(2)

# Main script execution
for email in email_list:
    visit_bookmyshow()
    click_im_interested()
    click_continue_with_email()
    enter_email(email)
    confirm_interest()
    sign_out()

driver.quit()
