import time
import random
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

download_path = r"E:\Python Automation Bot"

#Google Chrome
options = Options()
prefs = {"download.default_directory" : download_path}
options.add_experimental_option("prefs",prefs)

# Logging in 
PATH = "E:\chrome driver\chromedriver.exe"
driver = webdriver.Chrome(PATH, options=options)
driver.get("https://instagram.com")
username = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.NAME, "username")))
password = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.NAME, "password")))
username.clear()
password.clear()
username.send_keys("username_variable")
password.send_keys("password_variable")
login = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()



# Bypassing Prompts
time.sleep(3)
not_now_alert = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
not_now_alert = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
time.sleep(2)
# search = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='x9f619 xxk0z11 xvy4d1p x11xpdln xii2z7h x19c4wfv']/*[name()='svg'][@aria-label='Search']"))).click()
searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))

search_terms = []
searchbox.clear()
search_terms = random.choice(search_terms)
searchbox.send_keys(search_terms)
searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//a[@href='/{search_terms}/']"))).click()



# Selecting Reel From Instagram
reel_section_select = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//a[@href='/{search_terms}/reels/']"))).click()
time.sleep(3)
anchors = driver.find_elements(By.TAG_NAME, 'a')
anchors = [a.get_attribute('href') for a in anchors]
anchors = [a for a in anchors if str(a).startswith("https://www.instagram.com/reel/")]
print('Found ' + str(len(anchors)) + ' links to reels')
print(random.choice(anchors))




# Downloading reel from 3rd party software
driver.get("https://instavideosave.net/")
put_link_in_search = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.NAME, "search")))
put_link_in_search.click()
put_link_in_search.send_keys(random.choice(anchors))

download_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[@class=' mt-2 mr-3 p-1 bg-blue-600 w-[96px] flex justify-center h-10 items-center rounded text-white']/*[name()='svg'][@class='h-6 w-6 text-white']")))
download_button.click()
time.sleep(5)
download_button2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='mt-3 mb-3 pl-2 h-9 bg-blue-600 w-[70%] lg:w-[80%] flex justify-center items-center rounded text-white']/*[name()='svg'][@class='h-5 w-5 text-white ']")))
download_button2.click()

time.sleep(20)


# Uploading To YouTube

