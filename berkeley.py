from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import requests

#Initialize headlress browser
options = Options()
options.add_argument("--headless")
browser = webdriver.Firefox(options = options)
url = "https://apply.berkeley.edu/account/login?r=https%3a%2f%2fapply.berkeley.edu%2fapply%2fstatus"
#Hashed out for privacy
email = "#####"
password = "####"


browser.get(url)

#Inserts email address by finding element
def insertEmail():
    emailField = browser.find_element_by_id("email")
    emailField.send_keys(email)

#Inserts password by finding element
def insertPassword():
    passwordField = browser.find_element_by_id("password")
    passwordField.send_keys(password)
    
#Clicks the login button
def clickLoginButton():
    button = browser.find_element_by_class_name("default")
    button.click()


def login():
    insertEmail()
    insertPassword()
    clickLoginButton()

#Finds the textbox via css selector
def findUpdate():
    textField = browser.find_elements_by_css_selector('div.status_box:nth-child(2) > div:nth-child(3) > p:nth-child(2)')
    for value in textField:
        foundText = value.text
    return foundText

#Returns the status of the waitlist
def returnUpdateStatus():
    updateText = findUpdate()
    if(updateText.strip() == "An update to your application was last posted March 26, 2020."):
        status = "No update :("
    else:
        status = "There's an update!"
    print(status)
    return status
#the "main" function
def execute():
    login()
    return returnUpdateStatus()
    browser.quit()
execute()



