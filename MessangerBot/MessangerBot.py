import urllib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
#Opens facebook.com
driver.get("https://www.facebook.com/")

#Some tricks :)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[3]/label/input").click()

#Enter your email and password below
driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div[2]/form/div/div[1]/input").send_keys("Your email")
driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div[2]/form/div/div[2]/input").send_keys("Your password")

#Login button is being clicked
driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div[2]/form/div/div[3]/button").click()

#Messages is being opened and first chat is clicked
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[2]/div[2]/div[2]/div/a/div").click()
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[3]/div/div[1]/div/div/ul/li[1]/a/div").click()

for i in range(10):
	driver.find_element_by_xpath("/html/body/div[1]/div[7]/div[1]/div/div/div[4]/div/div[1]/div/div/div/div/div/div/div/div[2]/div[4]/div/div/div/span/div/div/div[2]/div/div/div/div").click()
	
	#Enter your message below
	driver.find_element_by_xpath("/html/body/div[1]/div[7]/div[1]/div/div/div[4]/div/div[1]/div/div/div/div/div/div/div/div[2]/div[4]/div/div/div/span/div/div/div[2]/div/div/div/div").send_keys("Enter a message.")
	driver.find_element_by_xpath("/html/body/div[1]/div[7]/div[1]/div/div/div[4]/div/div[1]/div/div/div/div/div/div[1]/div/div[2]/div[4]/div/div/div/span/div/div/div/div/div/div/div").send_keys(Keys.ENTER)
