import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

timeout = 15

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


for i in range(len(branches)):
    # input("Press ENTER/RETURN after creating an account or logging in to an existing account")
    input()
    
    WebDriverWait(driver,timeout).until(EC.presence_of_element_located((By.ID,"organization-name")))
    sleep(3)
    dept_name = driver.find_element(By.ID,"organization-name")
    dept_name.send_keys("BMSIT")
    
    checkbox_1 = driver.find_element(By.ID,"contact-info_customer_addresses_0__addressType_code-3")
    checkbox_1.click()

    address_1 = driver.find_element(By.ID,"address-line1")
    address_1.send_keys("Doddaballapur Main Road,Avalahalli")

    address_2 = driver.find_element(By.ID,"address-line2")
    address_2.send_keys("Yelahanka, Bengaluru, Karnataka 560064")

    city = driver.find_element(By.ID,"city")
    city.send_keys("Bengaluru")

    dropdown = driver.find_element(By.ID,"province")
    select_state = Select(dropdown)
    select_state.select_by_visible_text("Karnataka")

    pin_code = driver.find_element(By.ID,"postal-code")
    pin_code.send_keys("560064")

    telephone = driver.find_element(By.ID,"mobile-number")
    telephone.send_keys("+917760735073")

    # continue_button = driver.find_element(By.XPATH,"/html/body/div[6]/div[4]/div[1]/div[2]/div[3]/div/div[1]/div/div/div/div/div[6]/input")

    WebDriverWait(driver,timeout).until(EC.presence_of_element_located((By.ID,"mc-pr-checkout-sec")))
    
    continue_button = driver.find_element(By.ID,"mc-pr-checkout-sec")
    continue_button.click()

    sleep(5)

    search_college = driver.find_element(By.ID,"searchUniversity")
    search_college.click()

    WebDriverWait(driver,timeout).until(EC.presence_of_element_located((By.ID,"universityFilter")))

    search_box = driver.find_element(By.ID,"universityFilter")
    search_box.send_keys("BMS")
    

    sleep(2)

    bmsit = driver.find_element(By.LINK_TEXT,"BMS Institute of Technology")
    bmsit.click()

    undergrad = driver.find_element(By.ID,"studentStatusUndergraduate Student")
    undergrad.click()

    degree = driver.find_element(By.ID,"stud-degree-pursued")
    select_degree = Select(degree)
    select_degree.select_by_visible_text("Bachelor of Engineering")

    program = driver.find_element(By.ID,"stud-academic-program")
    select_program  = Select(program)
    select_program.select_by_visible_text(full_forms[branches[i]])

    grad_month = driver.find_element(By.ID,"estimated-grad-month")
    select_month = Select(grad_month)
    select_month.select_by_visible_text("August")

    grad_year = driver.find_element(By.ID,"estimated-grad-year")
    select_year = Select(grad_year)
    print(str(grad_years[i]))
    print(str(int(grad_years[i])))
    select_year.select_by_visible_text(str(int(grad_years[i])))

    field_of_study = driver.find_element(By.ID,"stud-current-study")
    select_field_of_study = Select(field_of_study)
    select_field_of_study.select_by_visible_text("Computer Sciences and Information Technologies")
    
    accreditation = driver.find_element(By.ID,"stud-prog-accredited")
    select_accreditation = Select(accreditation)
    select_accreditation.select_by_visible_text("Yes")
    
    tech_focus = driver.find_element(By.ID,"stud-technical-focus")
    select_tech_focus = Select(tech_focus)
    select_tech_focus.select_by_visible_text("Computing and Processing (Hardware/Software)")

    mem_dir = driver.find_element(By.ID,"memberdir-options1")
    mem_dir.click()

    input()

    # join_puspose = driver.find_element(By.ID,"additional-info")
    # check_boxes = join_puspose.find_element(By.ID,".//input[@type='checkbox']")
    
    # for check_box in check_boxes[:-1]:
    #     check_box.click()

    c1 = driver.find_element(By.ID,"TechnicallyCurrent")
    c1.click()
    c2 = driver.find_element(By.ID,"CareerOpurtunities")
    c2.click()
    c3 = driver.find_element(By.ID,"ExpandProfessionalNetwork")
    c3.click()
    c4 = driver.find_element(By.ID,"ConnectToLocalActivities")
    c4.click()
    c5 = driver.find_element(By.ID,"HumanitarianPrograms")
    c5.click()
    c6 = driver.find_element(By.ID,"Discounts")
    c6.click()

    referral = driver.find_element(By.ID,"member-referral")
    select_referral = Select(referral)
    select_referral.select_by_visible_text("Member referral")

    sleep(2)

    continue_button_2 = driver.find_element(By.XPATH,"/html/body/div[6]/div[4]/div[1]/div[2]/div[3]/div/div[1]/div/div/div/div/div[6]/input")
    continue_button_2.click()

    # WebDriverWait(driver,timeout).until(EC.presence_of_element_located((By.LINK_TEXT,"Society Memberships")))
    sleep(3)

    society_memberships = driver.find_element(By.LINK_TEXT,"Society Memberships")
    society_memberships.click()

    comp_society = driver.find_element(By.LINK_TEXT,"IEEE Computer Society Membership")
    comp_society.click()

    add_items = driver.find_element(By.ID,"add-product-button-id")
    add_items.click()

    catalog = driver.find_element(By.LINK_TEXT,"Catalog")
    catalog.click()

    society_memberships.click()

    for _ in range(4):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        sleep(2)

    i = i+1