import time
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import Login
import pandas as pd


df = pd.read_csv("v.csv")

# initial the text context that we want to send later
text_msg = "What's going on?"

# the login page of text free us website
textfree_login_url = "https://messages.textfree.us/login"

# initial our driver with seleniums
driver = webdriver.Chrome("/Users/maggiesun/Documents/ClassAIT/mkt_tech/yelp/chromedriver")
driver.get(textfree_login_url)
time.sleep(1)

try:
    # process login action
    driver.find_element_by_id('username').send_keys(Login.username)
    time.sleep(1)

    driver.find_element_by_id('password').send_keys(Login.pwd)
    time.sleep(3)

    #press the submit button to complete the login process
    driver.find_element_by_xpath("//button[@type = 'submit']").click()
    time.sleep(3)

    #press dismiss when the text free website pop up some suggestion
    driver.find_element_by_id("SyncContactsXDismissPopup").click()
    time.sleep(3)

finally:
    # loop through csv file to send our message
    for index, row in df.iterrows():
        # get into the text page
        driver.find_element_by_id("startNewConversationButton").click()
        time.sleep(1)

        # add the phone number from our csv file (the column of the phone is called "To")
        driver.find_element_by_id("contactInput").send_keys(row['To'])
        time.sleep(2)

        # add the text context that we initial above
        # you could also add customize name into the text_msg if you have the data in csv file
        driver.find_element_by_class_name("emojionearea-editor").send_keys(text_msg)
        time.sleep(2)

        # click the send button when we finish edit our text
        driver.find_element_by_xpath("//button[@type = 'submit']").click()
        time.sleep(3)

        # print out the phone numbers that we successfully send SMS to
        print("Phone: ", row['To'])
        print("-----------------------")
       

