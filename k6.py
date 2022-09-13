from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import tkinter as tk
import secrets
import random
import string
import os

###TEMP-NAMES###

t = random.randint(20,28)
t1 = random.randint(6,10)
t2 = random.randint(15,25)
t3 = random.randint(46,60)
driver = webdriver.Chrome()


driver.get("https://trxminer.fun/?ref=111862")

time.sleep(t)
driver.find_element(By.ID,"icon_prefix2").click()
time.sleep(t1)
driver.find_element(By.ID,"icon_prefix2").send_keys("TQP6aYDr147apWjXj96KpGhBNvC3MPMUUk")
time.sleep(t2)
driver.find_element(By.CLASS_NAME, "but_enter.btn-large.waves-effect.waves-light.red").click()
time.sleep(t3)






