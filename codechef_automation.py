'''
@author - ro4i7
'''


#importing libraries
from selenium import webdriver
from getpass import getpass
import time

# Credentials to login
username = "ro4i7"
password = getpass("Enter password: ")

# Problem code
problem_code = input("Problem code: ")

# Name of the submission code
submission_file = input("Submission file: ")

# Read submission file
with open(submission_file, 'r') as f:
	code = f.read()

# Download webdriver for your version of browser from here - https://selenium-python.readthedocs.io/installation.html#drivers
# I used web driver from chrome version 84
# Start a browser session
browser = webdriver.Chrome()

# Open Codechef in browser
browser.get("https://codechef.com")

# Accepting cookies
try:
    browser.find_element_by_id("gdpr-i-love-cookies").click()
except:
    pass

# login into codechef
username_element = browser.find_element_by_id('edit-name')
username_element.send_keys(username)

password_element = browser.find_element_by_id('edit-pass')
password_element.send_keys(password)

browser.find_element_by_id('edit-submit').click()

# Open submission page
browser.get("https://www.codechef.com/submit/" + problem_code)

# wait for page to open
time.sleep(10)

# Click on toggle button to open simple text mode
browser.find_element_by_id("edit_area_toggle_checkbox_edit-program").click()

# Change the Programming language
code_language = browser.find_element_by_id("edit-language")
code_language.send_keys("C++14(gcc6.3)")

# Write and submit the code
code_element = browser.find_element_by_id("edit-program")
code_element.send_keys(code)

browser.find_element_by_id("edit-submit-1").click()

# wait for submission
time.sleep(10)

# get result
result = browser.find_element_by_id("display_result").text

print(result)
