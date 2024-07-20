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
        WebDriverWait(self.driver, 180).until(EC.presence_of_element_located((By.ID, 'username'))).send_keys(
            "09307212580")
        time.sleep(3)
        WebDriverWait(self.driver, 180).until(EC.presence_of_element_located((By.ID, 'send-otp-form-btn'))).click()
        time.sleep(8)
        WebDriverWait(self.driver, 180).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/main/div/div/div[2]/a[1]'))).click()
        WebDriverWait(self.driver, 180).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div/div/div/main/div/div/div/div/div[1]/div/div[2]/div/div[3]'))).click()
        WebDriverWait(self.driver, 180).until(
            EC.presence_of_element_located((By.XPATH,
                                            '/html/body/div/div/div/main/div/div/div/div/div[2]/div/div[2]/div/div[1]/a/div[2]/a'))).click()
        WebDriverWait(self.driver, 180).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div/div/div/main/div/div/div/div/div[2]/a[2]'))).click()
        while True:
            self.select_option_by_text(
                "/html/body/div/div/div[2]/div/div/div[2]/form/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[1]/div[1]",
                "سپه")
            dropdown = Select(
                WebDriverWait(self.driver, 180).until(EC.presence_of_element_located(
                    (By.XPATH, '/html/body/div/div/div[2]/div/div/div[2]/form/div[3]/div/div/div/div[1]/div[2]/div'))))
            if len(dropdown.options) > 1:
                dropdown.select_by_index(1)
                WebDriverWait(self.driver, 180).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '/html/body/div/div/div[2]/div/div/div[3]/button'))).click()
                break
            else:
                self.driver.refresh()
                WebDriverWait(self.driver, 180).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '/html/body/div/div/div/main/div/div/div/div/div[2]/a[2]'))).click()

    def select_option_by_text(self, element_xpath, option_text):
        try:
            dropdown = Select(
                WebDriverWait(self.driver, 180).until(EC.presence_of_element_located((By.XPATH, element_xpath))))
            dropdown.select_by_visible_text(option_text)
        except Exception as e:
            print(f"Error selecting option: {e}")

    def select_second_option(self, element_xpath):
        try:
            dropdown = Select(
                WebDriverWait(self.driver, 180).until(EC.presence_of_element_located((By.XPATH, element_xpath))))
            if len(dropdown.options) > 1:
                dropdown.select_by_index(1)
            else:
                print(f"We didn't select a second option")
        except Exception as e:
            print(f"Error selecting second option: {e}")


vam = Vam()
vam.entery_form()
