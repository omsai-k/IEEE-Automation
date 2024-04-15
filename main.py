import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep

membership_data = "Membership.xlsx"
df = pd.read_excel(membership_data)

names = df["Name"].tolist()
emails = df["Email"].tolist()


driver = webdriver.Edge()     #"/Users/omsai/Downloads"/chromedriver_mac_arm64

driver.get("https://www.ieee.org")
driver.maximize_window()

join_button = driver.find_element(By.XPATH,"/html/body/div[4]/header/div[2]/div[1]/div/div/div[2]/div[1]/a")
join_button.click()

join_as_student = driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div[4]/div/div[3]/div[1]/div[1]/div/div[3]/div[1]/div[2]/div/div[1]/a")
join_as_student.click()

# create_account = driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/input")
# create_account.click()

input("Press ENTER/RETURN after creating an account or logging in to an existing account")

dept_name = driver.find_element(By.XPATH,"/html/body/div[6]/div[4]/div[1]/div[1]/div[2]/div[2]/div[2]/div/div/div[4]/div/div[6]/div/div/form/fieldset/div/div/div[1]/div/div[4]/div/input")
dept_name.send_keys("BMSIT")

checkbox_1 = driver.find_element(By.XPATH,"/html/body/div[6]/div[4]/div[1]/div[1]/div[2]/div[2]/div[2]/div/div/div[4]/div/div[6]/div/div/form/fieldset/div/div/div[1]/div/div[5]/div/div/div[2]/div[3]/input")
checkbox_1.click()

address_1 = driver.find_element(By.XPATH,"/html/body/div[6]/div[4]/div[1]/div[1]/div[2]/div[2]/div[2]/div/div/div[4]/div/div[6]/div/div/form/fieldset/div/div/div[1]/div/div[6]/div[1]/input")
address_1.send_keys("Doddaballapur Main Road,Avalahalli")

address_2 = driver.find_element(By.XPATH,"/html/body/div[6]/div[4]/div[1]/div[1]/div[2]/div[2]/div[2]/div/div/div[4]/div/div[6]/div/div/form/fieldset/div/div/div[1]/div/div[7]/div/input")
address_2.send_keys("Yelahanka, Bengaluru, Karnataka 560064")

city = driver.find_element(By.XPATH,"/html/body/div[6]/div[4]/div[1]/div[1]/div[2]/div[2]/div[2]/div/div/div[4]/div/div[6]/div/div/form/fieldset/div/div/div[1]/div/div[8]/div[2]/div/input")
city.send_keys("Bengaluru")

dropdown = driver.find_element(By.XPATH,"/html/body/div[6]/div[4]/div[1]/div[1]/div[2]/div[2]/div[2]/div/div/div[4]/div/div[6]/div/div/form/fieldset/div/div/div[1]/div/div[8]/div[3]/div/select")
select_state = Select(dropdown)
select_state.select_by_visible_text("Karnataka")

pin_code = driver.find_element(By.XPATH,"/html/body/div[6]/div[4]/div[1]/div[1]/div[2]/div[2]/div[2]/div/div/div[4]/div/div[6]/div/div/form/fieldset/div/div/div[1]/div/div[8]/div[4]/div/input")
pin_code.send_keys("560064")

telephone = driver.find_element(By.XPATH,"/html/body/div[6]/div[4]/div[1]/div[1]/div[2]/div[2]/div[2]/div/div/div[4]/div/div[6]/div/div/form/fieldset/div/div/div[3]/div[2]")
telephone.send_keys("+917760735073")

continue_button = driver.find_element(By.XPATH,"/html/body/div[6]/div[4]/div[1]/div[2]/div[3]/div/div[1]/div/div/div/div/div[6]/input")
continue_button.click()

search_college = driver.find_element(By.XPATH,"/html/body/div[6]/div[4]/div[1]/div[1]/div[2]/div[3]/div[2]/div/div/div[4]/div/div[6]/div/div/div/div[1]/div/form/fieldset/div/div/div[2]/div[3]/input")
search_college.click()

search_box = driver.find_element(By.XPATH,"/html/body/div[6]/div[4]/div[1]/div[1]/div[2]/div[3]/div[2]/div/div/div[4]/div/div[6]/div/div/div/div[1]/div/form/fieldset/div/div/div[3]/div/div/div/div[1]/div[2]/div[2]/div/input")
search_box.send_keys("BMS")
sleep(2)

bmsit = driver.find_element(By.XPATH,"/html/body/div[6]/div[4]/div[1]/div[1]/div[2]/div[3]/div[2]/div/div/div[4]/div/div[6]/div/div/div/div[1]/div/form/fieldset/div/div/div[3]/div/div/div/div[1]/div[5]/div[1]/a")
bmsit.click()

undergrad = driver.find_element(By.XPATH,"/html/body/div[6]/div[4]/div[1]/div[1]/div[2]/div[3]/div[2]/div/div/div[4]/div/div[6]/div/div/div/div[1]/div/form/fieldset/div/div/div[5]/div[2]/div[1]/input")
undergrad.click()


degree = driver.find_element(By.XPATH,"/html/body/div[6]/div[4]/div[1]/div[1]/div[2]/div[3]/div[2]/div/div/div[4]/div/div[6]/div/div/div/div[1]/div/form/fieldset/div/div/div[7]/div/select[3]")
select_degree = Select(degree)
select_degree.select_by_visible_text("Bachelor of Engineering")



sleep(5)
