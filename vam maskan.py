import os
import time
import base64
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import tensorflow as tf
import subprocess
import sys
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
import re


class Vam():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://saman.mrud.ir/")

    def entery_form(self):
        WebDriverWait(self.driver, 180).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/main/div/div/div[2]/a[1]'))).click()
        WebDriverWait(self.driver, 180).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div/div/div/main/div/div/div/div[1]/div/div/a'))).click()
        WebDriverWait(self.driver, 180).until(EC.presence_of_element_located((By.ID, 'username'))).send_keys("09363920053")
        time.sleep(3)
        WebDriverWait(self.driver, 180).until(EC.presence_of_element_located((By.ID, 'send-otp-form-btn'))).click()
        time.sleep(8)
        WebDriverWait(self.driver, 180).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/main/div/div/div[2]/a[1]'))).click()
        WebDriverWait(self.driver, 180).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/main/div/div/div/div/div[1]/div/div[2]/div/div[3]'))).click()


vam = Vam()
vam.entery_form()