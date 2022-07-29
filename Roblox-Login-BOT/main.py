# by fluxeewe
# dont copy skid 
# github/fluxeewe24 
# ! yes(this is token grabber) 

from tkinter import Button
from selenium import webdriver
from pynput.mouse import Button, Controller

driver = webdriver.Chrome()
driver.get("https://www.roblox.com/login")
mouse = Controller()

f = open("login.txt", "r")

# config tu zjebie jeabny
usernameStr = f.readlines(1)
passwordStr = f.readlines(2)

username = driver.find_element_by_id('login-username')
username.send_keys(usernameStr)

password = driver.find_element_by_id('login-password')
password.send_keys(passwordStr)

mouse.position = (917, 277)
mouse.click(Button.left)

signInButton = driver.find_element_by_id('login-button')
signInButton.click()
