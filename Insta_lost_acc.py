'''
Basically retrieve the following list of the old account (using a follower's account)
Save the list to a file (so that the script doesn't have to retrieve the list every time, saves time)
Use the list and selenium to automate the following process on the new account
'''

import instaloader
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time, urllib.request
import requests

L = instaloader.Instaloader()

L.login("username", "password")

profile = instaloader.Profile.from_username(L.context, "acc_username")

#Record list of followers
file = open("followee_list.txt", "a")
for followee in profile.get_followees():
    file.write(followee.username+"\n")

file.close()

print("All followers retrieved!")


with open("remaining_followees.txt", "r") as file:
    followee_list = file.readlines()
    
driver = webdriver.Chrome()

driver.get("https://www.instagram.com/")

time.sleep(5)
username=driver.find_element(by=By.CSS_SELECTOR, value="input[name='username']")
password=driver.find_element(by=By.CSS_SELECTOR, value="input[name='password']")
username.clear()
password.clear()
username.send_keys("tiffyz_thisisnewmynewaccount")
password.send_keys("aroundusisverypopular")
login = driver.find_element(by=By.CSS_SELECTOR, value="button[type='submit']").click()

#save your login info?
wait = WebDriverWait(driver, 10)
notnow = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()
notnow2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()

#searchbox
for username in followee_list:
    time.sleep(2)
    searchbox=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='Search']")))
    searchbox.clear()
    searchbox.send_keys(username)
    time.sleep(1)
    searchbox=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='Search']")))
    searchbox.send_keys(Keys.ENTER)
    time.sleep(1)
    searchbox=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='Search']")))
    searchbox.send_keys(Keys.ENTER)
    time.sleep(4)
    try:
        follow_btn1 = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Follow')]")))
        #follow_btn1 = driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Follow')]")
        follow_btn1.click()
    except:
        print("Failed: ", username)
        pass

driver.Quit()
print("Done!")

