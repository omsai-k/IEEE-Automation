import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


driver = webdriver.Edge()     #"/Users/omsai/Downloads"/chromedriver_mac_arm64

driver.get("https://www.ieee.org")
driver.maximize_window()

join_button = driver.find_element(By.XPATH,"/html/body/div[4]/header/div[2]/div[1]/div/div/div[2]/div[1]/a")
join_button.click()

join_as_student = driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div[4]/div/div[3]/div[1]/div[1]/div/div[3]/div[1]/div[2]/div/div[1]/a")
join_as_student.click()

create_account = driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/input")
create_account.click()




sleep(5)
