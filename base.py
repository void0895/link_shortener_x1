from selenium import webdriver
from utils import generate_random_user_agent
import time


user_agent = generate_random_user_agent()

browser_path='/usr/bin/thorium-browser'
options = webdriver.ChromeOptions()
options.binary_location = browser_path
# You can customize other browser options as needed 
# options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument(f"user-agent={user_agent}") 
driver = webdriver.Chrome(options=options) 
driver.get("https://urllinkshort.in/3OL3") 


time.sleep(120)
