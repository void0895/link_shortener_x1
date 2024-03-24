from selenium import webdriver
from utils import generate_random_user_agent, time_cal
import time
from clicks import clk
user_agent = generate_random_user_agent()


@time_cal
def create_driver(user_agent):
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
    

@time_cal
def test_alpha():
    driver = create_driver(user_agent)
    driver.get("https://urllinkshort.in/3OL3")
    clk(driver, "suntechu.in", method="partial_link_text")
    print("t1")
    clk(driver, "CloseAd", method="id", click_method="js", time=5, show_error=False)
    print("t2")
    clk(driver, "Dual Tap Fast", method="partial_link_text", click_method="js", time=20)
    print("t3")
    clk(driver, '//*[@id="rtg7"]', method="xpath", click_method="action_chains", time=20)
    print("t4")
    clk(driver, "CloseAd", method="id", click_method="js", time=5, show_error=False)
    print("t5")
    clk(driver, '#rtg-generate > center > button', method="css_selector", click_method="js", time=20)
    print("t6")
    clk(driver, "#rtg-snp2", method="css_selector", click_method="js", time=20)
    print("t7")
    clk(driver, "CloseAd", method="id", click_method="js", time=5, show_error=False)
    print("t8")
    clk(driver, "/html/body/section/div/div/div/div/div[1]/a", method="xpath", click_method="action_chains")
    time.sleep(20)


test_alpha()
time.sleep(60)
