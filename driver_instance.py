# driver_instance.py

from utils import time_cal

@time_cal
def create_driver():
    from utils import generate_random_user_agent
    from selenium import webdriver
    user_agent = generate_random_user_agent()
    browser_path='/usr/bin/thorium-browser'
    options = webdriver.ChromeOptions()
    options.binary_location = browser_path
    # You can customize other browser options as needed 
    # options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(f"user-agent={user_agent}")
    options.add_argument("--disable-images") 
    options.add_argument("--disable-javascript")
    options.page_load_strategy = 'eager' 
    
    driver = webdriver.Chrome(options=options) 
    return driver



# How to use 

# from driver_instance import create_driver
# dx = create_driver()
# dx.get("https://example.com")
# dx.quit()