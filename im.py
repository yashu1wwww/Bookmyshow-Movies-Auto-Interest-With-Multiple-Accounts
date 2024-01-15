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

#replace with your 15 dot mails of one gmails and another 15 dot mails of another gmails here remaining all goes automatic process you only enter the otp in 11 seconds(use mobile for otp where fastly we can enter by seeing otp in mobile)....

a=['mygmail+nash@gmail.com']
b=['mygmail@gmail.com'] 
c=['my@gmail.com'] 
d=['my@gmail.com']
e=['my@gmail.com']
f=['my@gmail.com']
g=['mygmail+marva@gmail.com']
h=['my@gmail.com']
i=['mygmail+derik@gmail.com']
j=['mygmail+alvie@gmail.com']
k=['my@gmail.com']
l=['mygmail+gage@gmail.com']
m=['mygmail+max@gmail.com']
n=['my@gmail.com']
o=['mygmail+lita@gmail.com']
#here i added another id dot mails
p=['mygmail+ginny@gmail.com']
q=['mygmail+timmy@gmail.com']
r=['mygmail+kent@gmail.com']
t=['mygmail+kali@gmail.com']
u=['mygmail+bryce@gmail.com']
v=['my@gmail.com']
w=['mygmail+rosie@gmail.com']
x=['mygmail+madge@gmail.com']
y=['my@gmail.com']
z=['mygmail+keily@gmail.com']
aa=['my@gmail.com']
bb=['mygmail+evans@gmail.com']
cc=['mygmail+stan@gmail.com']
dd=['mygmail+kaye@gmail.com']


option = webdriver.ChromeOptions()
option.add_experimental_option("debuggerAddress","localhost:9222")

driver = webdriver.Chrome(options=option)

time.sleep(2)

driver.get("https://in.bookmyshow.com") #select these text and press ctrl+h then ask find what and replace with movie url with city

time.sleep(5)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interested button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #ask for email 

time.sleep(2)

driver.find_element_by_xpath('//*[@id="emailId"]').send_keys(random.choice(a)) #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #click on next button

time.sleep(15) #within 15 second enter the otp..

driver.maximize_window()

driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interest cofirm button..

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com") #first select the city then select the required movie url and replace here..

time.sleep(5)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interested button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #ask for email 

time.sleep(2)

driver.find_element_by_xpath('//*[@id="emailId"]').send_keys(random.choice(b)) #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #click on next button

time.sleep(15) #within 15 second enter the otp..

driver.maximize_window()

driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interest cofirm button..

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com") #first select the city then select the required movie url and replace here..

time.sleep(5)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interested button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #ask for email 

time.sleep(2)

driver.find_element_by_xpath('//*[@id="emailId"]').send_keys(random.choice(c)) #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #click on next button

time.sleep(15) #within 15 second enter the otp..

driver.maximize_window()

driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interest cofirm button..

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com") #first select the city then select the required movie url and replace here..

time.sleep(5)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interested button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #ask for email 

time.sleep(2)

driver.find_element_by_xpath('//*[@id="emailId"]').send_keys(random.choice(d)) #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #click on next button

time.sleep(15) #within 15 second enter the otp..

driver.maximize_window()

driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interest cofirm button..

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com") #first select the city then select the required movie url and replace here..

time.sleep(5)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interested button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #ask for email 

time.sleep(2)

driver.find_element_by_xpath('//*[@id="emailId"]').send_keys(random.choice(e)) #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #click on next button

time.sleep(15) #within 15 second enter the otp..

driver.maximize_window()

driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interest cofirm button..

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com") #first select the city then select the required movie url and replace here..

time.sleep(5)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interested button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #ask for email 

time.sleep(2)

driver.find_element_by_xpath('//*[@id="emailId"]').send_keys(random.choice(f)) #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #click on next button

time.sleep(15) #within 15 second enter the otp..

driver.maximize_window()

driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interest cofirm button..

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com") #first select the city then select the required movie url and replace here..

time.sleep(5)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interested button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #ask for email 

time.sleep(2)

driver.find_element_by_xpath('//*[@id="emailId"]').send_keys(random.choice(g)) #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #click on next button

time.sleep(15) #within 15 second enter the otp..

driver.maximize_window()

driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interest cofirm button..

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com") #first select the city then select the required movie url and replace here..

time.sleep(5)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interested button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #ask for email 

time.sleep(2)

driver.find_element_by_xpath('//*[@id="emailId"]').send_keys(random.choice(h)) #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #click on next button

time.sleep(15) #within 15 second enter the otp..

driver.maximize_window()

driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interest cofirm button..

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com") #first select the city then select the required movie url and replace here..

time.sleep(5)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interested button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #ask for email 

time.sleep(2)

driver.find_element_by_xpath('//*[@id="emailId"]').send_keys(random.choice(i)) #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #click on next button

time.sleep(15) #within 15 second enter the otp..

driver.maximize_window()

driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interest cofirm button..

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com") #first select the city then select the required movie url and replace here..

time.sleep(5)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interested button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #ask for email 

time.sleep(2)

driver.find_element_by_xpath('//*[@id="emailId"]').send_keys(random.choice(j)) #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #click on next button

time.sleep(15) #within 15 second enter the otp..

driver.maximize_window()

driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interest cofirm button..

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com") #first select the city then select the required movie url and replace here..

time.sleep(5)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interested button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #ask for email 

time.sleep(2)

driver.find_element_by_xpath('//*[@id="emailId"]').send_keys(random.choice(k)) #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #click on next button

time.sleep(15) #within 15 second enter the otp..

driver.maximize_window()

driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interest cofirm button..

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com") #first select the city then select the required movie url and replace here..

time.sleep(5)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interested button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #ask for email 

time.sleep(2)

driver.find_element_by_xpath('//*[@id="emailId"]').send_keys(random.choice(l)) #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #click on next button

time.sleep(15) #within 15 second enter the otp..

driver.maximize_window()

driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interest cofirm button..

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com") #first select the city then select the required movie url and replace here..

time.sleep(5)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interested button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #ask for email 

time.sleep(2)

driver.find_element_by_xpath('//*[@id="emailId"]').send_keys(random.choice(m)) #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #click on next button

time.sleep(15) #within 15 second enter the otp..

driver.maximize_window()

driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interest cofirm button..

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com") #first select the city then select the required movie url and replace here..

time.sleep(5)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interested button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #ask for email 

time.sleep(2)

driver.find_element_by_xpath('//*[@id="emailId"]').send_keys(random.choice(n)) #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #click on next button

time.sleep(15) #within 15 second enter the otp..

driver.maximize_window()

driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interest cofirm button..

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com") #first select the city then select the required movie url and replace here..

time.sleep(5)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interested button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #ask for email 

time.sleep(2)

driver.find_element_by_xpath('//*[@id="emailId"]').send_keys(random.choice(o)) #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #click on next button

time.sleep(15) #within 15 second enter the otp..

driver.maximize_window()

driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interest cofirm button..

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com") #first select the city then select the required movie url and replace here..

time.sleep(5)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interested button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #ask for email 

time.sleep(2)

driver.find_element_by_xpath('//*[@id="emailId"]').send_keys(random.choice(p)) #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #click on next button

time.sleep(15) #within 15 second enter the otp..

driver.maximize_window()

driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interest cofirm button..

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com") #first select the city then select the required movie url and replace here..

time.sleep(5)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interested button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #ask for email 

time.sleep(2)

driver.find_element_by_xpath('//*[@id="emailId"]').send_keys(random.choice(q)) #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #click on next button

time.sleep(15) #within 15 second enter the otp..

driver.maximize_window()

driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interest cofirm button..

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com") #first select the city then select the required movie url and replace here..

time.sleep(5)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interested button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #ask for email 

time.sleep(2)

driver.find_element_by_xpath('//*[@id="emailId"]').send_keys(random.choice(r)) #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #click on next button

time.sleep(15) #within 15 second enter the otp..

driver.maximize_window()

driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interest cofirm button..

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com") #first select the city then select the required movie url and replace here..

time.sleep(5)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interested button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #ask for email 

time.sleep(2)

driver.find_element_by_xpath('//*[@id="emailId"]').send_keys(random.choice(s)) #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #click on next button

time.sleep(15) #within 15 second enter the otp..

driver.maximize_window()

driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interest cofirm button..

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com") #first select the city then select the required movie url and replace here..

time.sleep(5)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interested button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #ask for email 

time.sleep(2)

driver.find_element_by_xpath('//*[@id="emailId"]').send_keys(random.choice(t)) #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #click on next button

time.sleep(15) #within 15 second enter the otp..

driver.maximize_window()

driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interest cofirm button..

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com") #first select the city then select the required movie url and replace here..

time.sleep(5)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interested button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #ask for email 

time.sleep(2)

driver.find_element_by_xpath('//*[@id="emailId"]').send_keys(random.choice(u)) #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #click on next button

time.sleep(15) #within 15 second enter the otp..

driver.maximize_window()

driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interest cofirm button..

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com") #first select the city then select the required movie url and replace here..

time.sleep(5)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interested button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #ask for email 

time.sleep(2)

driver.find_element_by_xpath('//*[@id="emailId"]').send_keys(random.choice(v)) #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #click on next button

time.sleep(15) #within 15 second enter the otp..

driver.maximize_window()

driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interest cofirm button..

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com") #first select the city then select the required movie url and replace here..

time.sleep(5)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interested button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #ask for email 

time.sleep(2)

driver.find_element_by_xpath('//*[@id="emailId"]').send_keys(random.choice(w)) #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #click on next button

time.sleep(15) #within 15 second enter the otp..

driver.maximize_window()

driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interest cofirm button..

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)
driver.get("https://in.bookmyshow.com") #first select the city then select the required movie url and replace here..

time.sleep(5)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interested button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #ask for email 

time.sleep(2)

driver.find_element_by_xpath('//*[@id="emailId"]').send_keys(random.choice(x)) #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #click on next button

time.sleep(15) #within 15 second enter the otp..

driver.maximize_window()

driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interest cofirm button..

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com") #first select the city then select the required movie url and replace here..

time.sleep(5)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interested button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #ask for email 

time.sleep(2)

driver.find_element_by_xpath('//*[@id="emailId"]').send_keys(random.choice(y)) #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #click on next button

time.sleep(15) #within 15 second enter the otp..

driver.maximize_window()

driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interest cofirm button..

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com") #first select the city then select the required movie url and replace here..

time.sleep(5)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interested button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #ask for email 

time.sleep(2)

driver.find_element_by_xpath('//*[@id="emailId"]').send_keys(random.choice(z)) #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #click on next button

time.sleep(15) #within 15 second enter the otp..

driver.maximize_window()

driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interest cofirm button..

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com") #first select the city then select the required movie url and replace here..

time.sleep(5)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interested button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #ask for email 

time.sleep(2)

driver.find_element_by_xpath('//*[@id="emailId"]').send_keys(random.choice(aa)) #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #click on next button

time.sleep(15) #within 15 second enter the otp..

driver.maximize_window()

driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interest cofirm button..

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com") #first select the city then select the required movie url and replace here..

time.sleep(5)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interested button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #ask for email 

time.sleep(2)

driver.find_element_by_xpath('//*[@id="emailId"]').send_keys(random.choice(bb)) #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #click on next button

time.sleep(15) #within 15 second enter the otp..

driver.maximize_window()

driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interest cofirm button..

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com") #first select the city then select the required movie url and replace here..

time.sleep(5)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interested button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #ask for email 

time.sleep(2)

driver.find_element_by_xpath('//*[@id="emailId"]').send_keys(random.choice(cc)) #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #click on next button

time.sleep(15) #within 15 second enter the otp..

driver.maximize_window()

driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interest cofirm button..

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(2)

driver.get("https://in.bookmyshow.com") #first select the city then select the required movie url and replace here..

time.sleep(5)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interested button

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click() #ask for email 

time.sleep(2)

driver.find_element_by_xpath('//*[@id="emailId"]').send_keys(random.choice(dd)) #email select

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click() #click on next button

time.sleep(15) #within 15 second enter the otp..

driver.maximize_window()

driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click() #click on i'm interest cofirm button..

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/header/div[1]/div/div/div/div[2]/div[2]').click() #click on human logo

time.sleep(2)

driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/div[2]/div/div[3]/button').click() #signout

time.sleep(20)

#<𝙏𝙚𝙢𝙥 𝙈𝙖𝙞𝙡𝙨📧>

# https://generator.email/

# https://temp-mail.org/

# https://mail.tm/en/

# https://www.fakemail.net/

# https://tempail.com/


