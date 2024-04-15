import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep

membership_data = "Membership.xlsx"
df = pd.read_excel(membership_data)

# names = df["Name"].tolist()
# emails = df["Email"].tolist()
branches = df["Branch"].tolist()
grad_years = df["YEAR OF GRADUATION"].tolist()


full_forms = {
    "CSE":"Computer Science",
    "ISE":"Information Science",
    "ECE":"Electronics & Communications",
    "ETE":"Electronics & Telecomm Engrg",
    "AIML":"Artificial Intelligence",
    "CSBS":"Computer Systems"
}

driver = webdriver.Edge()

driver.get("https://www.ieee.org")
driver.maximize_window()

join_button = driver.find_element(By.XPATH,"/html/body/div[4]/header/div[2]/div[1]/div/div/div[2]/div[1]/a")
join_button.click()

join_as_student = driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div[4]/div/div[3]/div[1]/div[1]/div/div[3]/div[1]/div[2]/div/div[1]/a")
join_as_student.click()

i = 0

while(True):
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

    program = driver.find_element(By.XPATH,"/html/body/div[6]/div[4]/div[1]/div[1]/div[2]/div[3]/div[2]/div/div/div[4]/div/div[6]/div/div/div/div[1]/div/form/fieldset/div/div/div[10]/div/select")
    select_program  = Select(program)
    select_program.select_by_visible_text(full_forms[branches[i]])

    grad_month = driver.find_element("/html/body/div[6]/div[4]/div[1]/div[1]/div[2]/div[3]/div[2]/div/div/div[4]/div/div[6]/div/div/div/div[1]/div/form/fieldset/div/div/div[13]/div[1]/select")
    select_month = Select(grad_month)
    select_month.select_by_visible_text("August")

    grad_year = driver.find_element(By.XPATH,"/html/body/div[6]/div[4]/div[1]/div[1]/div[2]/div[3]/div[2]/div/div/div[4]/div/div[6]/div/div/div/div[1]/div/form/fieldset/div/div/div[13]/div[2]/select")
    select_year = Select(grad_year)
    select_year.select_by_visible_text(grad_years[i])

    field_of_study = driver.find_element(By.XPATH,"/html/body/div[6]/div[4]/div[1]/div[1]/div[2]/div[3]/div[2]/div/div/div[4]/div/div[6]/div/div/div/div[1]/div/form/fieldset/div/div/div[14]/div/select")
    select_field_of_study = Select(field_of_study)
    select_field_of_study.select_by_visible_text("Computer Sciences and Information Technologies")
    
    tech_focus = driver.find_element(By.XPATH,"/html/body/div[6]/div[4]/div[1]/div[1]/div[2]/div[3]/div[2]/div/div/div[4]/div/div[6]/div/div/div/div[1]/div/form/fieldset/div/div/div[17]/div/select")
    select_tech_focus = Select(tech_focus)
    select_tech_focus.select_by_visible_text("Computing and Processing (Hardware/Software)")

    mem_dir = driver.find_element(By.XPATH,"/html/body/div[6]/div[4]/div[1]/div[1]/div[2]/div[4]/div[2]/div/div/div[4]/div/div[6]/div/div/form/div[1]/div/div/div/div[1]/div[1]/input")
    mem_dir.click()

    join_puspose = driver.find_element(By.XPATH,"/html/body/div[6]/div[4]/div[1]/div[1]/div[2]/div[4]/div[2]/div/div/div[4]/div/div[6]/div/div/form/div[4]/div")
    check_boxes = join_puspose.find_element(By.XPATH,".//input[@type='checkbox']")
    
    for check_box in check_boxes[:-1]:
        check_box.click()

    referral = driver.find_element(By.XPATH,"/html/body/div[6]/div[4]/div[1]/div[1]/div[2]/div[4]/div[2]/div/div/div[4]/div/div[6]/div/div/form/fieldset/div[1]/div/select")
    select_referral = Select(referral)
    select_referral.select_by_visible_text("Member referral")

    continue_button.click()

    society_memberships = driver.find_element(By.XPATH,"/html/body/div[4]/div[4]/div[1]/div[1]/div[5]/div[2]/div/div/div[2]/div/div")
    society_memberships.click()

    comp_society = driver.find_element(By.XPATH,"/html/body/div[4]/div[4]/div[1]/div[1]/div[3]/div[4]/div/div[14]/div[2]/p[1]/a")
    comp_society.click()

    add_items = driver.find_element(By.XPATH,"/html/body/div[4]/div[4]/div[1]/div[1]/div[6]/div[3]/div/div[2]/div[1]/div/div/div[1]/div/div[6]/div/div/div[1]/input")
    add_items.click()

    catalog = driver.find_element("/html/body/div[4]/div[4]/div[1]/div[1]/div[1]/div[1]/h1/a")
    catalog.click()

    society_memberships.click()

    for _ in range(4):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        sleep(2)

    i = i+1
