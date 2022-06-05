from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://in.bookmyshow.com/bengaluru/movies/kranti/ET00323056")

input=driver.find_element_by_xpath('//*[@id="wzrk-confirm"]').click()

input=driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span').click()

#time.sleep(4)

input=driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

input=driver.find_element_by_xpath('//*[@id="emailId"]')
input.send_keys("yashwanth6678@gmail.com") #replace with your email otp will come you must enter it otp will not fill automatically

input=driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

time.sleep(2)






