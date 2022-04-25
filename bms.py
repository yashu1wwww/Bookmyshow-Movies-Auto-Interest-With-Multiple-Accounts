from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://in.bookmyshow.com/bengaluru/movies/kranti/ET00323056")

input=driver.find_element_by_xpath('//*[@id="wzrk-confirm"]')
input.click()

input=driver.find_element_by_xpath('//*[@id="super-container"]/div[2]/section[1]/div/div/div[2]/section/div[2]/div[2]/button/span')
input.click()

input=driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div')
input.click()

input=driver.find_element_by_xpath('//*[@id="emailId"]')
input.send_keys("beroyal123@gmail.com")

input=driver.find_element_by_xpath('//*[@id="super-container"]/div[3]/div/div/div/div[2]/form/div[2]/button')
input.click()





