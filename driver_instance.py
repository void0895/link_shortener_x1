# driver_instance.py

from utils import time_cal

@time_cal
def create_driver():
    from utils import generate_random_user_agent
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    user_agent = generate_random_user_agent()
    browser_path='/usr/bin/thorium-browser'
    driver_path='/opt/thorium-browser/chromedriver'
    options = Options()
    options.binary_location = browser_path
    service = Service(driver_executable_path=driver_path)
    # You can customize other browser options as needed 
    # options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(f"user-agent={user_agent}")
    options.add_argument("--disable-image-loading") 
    options.add_argument("--disable-javascript")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument('--remote-debugging-pipe')
    #options.add_argument("--headless")
    options.page_load_strategy = 'eager' 
    driver = webdriver.Chrome(service=service, options=options) 
    return driver



@time_cal
def bypass_driver(headless=1, save=0, random=1):
    from utils import generate_random_user_agent
    import undetected_chromedriver as uc
    user_agent = generate_random_user_agent()
    browser_path='/usr/bin/thorium-browser'
    driver_path='/opt/thorium-browser/chromedriver'
    options = uc.ChromeOptions()
    options.binary_location = browser_path
    if random == 1:
        options.add_argument(f"--user-agent={user_agent}")
    options.add_argument("--disable-image-loading") 
    options.add_argument("--disable-javascript")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    if headless == 0:
        options.add_argument("--headless=new")
    options.add_argument("--disable-extensions")
    options.page_load_strategy = 'none'
    options.add_argument("--disk-cache-dir=disk_cache")
    if save:
        options.add_argument(f"--user-data-dir={save}")
    driver = uc.Chrome(driver_executable_path=driver_path, options=options, version_main = 122)
    return driver
    
# How to use 

# from driver_instance import create_driver
# dx = create_driver()
# dx.get("https://example.com")
# dx.quit()
