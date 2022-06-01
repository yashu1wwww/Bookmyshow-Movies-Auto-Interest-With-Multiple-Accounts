from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://in.bookmyshow.com/login/?referer=/bengaluru/movies/kranti/ET00323056")

input=driver.find_element_by_xpath('//*[@id="wzrk-confirm"]').click()

input=driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div').click()

input=driver.find_element_by_xpath('//*[@id="emailId"]')
input.send_keys("vkdhoni123@gmail.com") #Replace Your Mail OTP Will Not Be Entered Automatically You Must Enter That

input=driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button').click()

#In Last It Ask Select City Select it👍





