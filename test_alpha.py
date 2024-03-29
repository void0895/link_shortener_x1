# Test alpha

from driver_instance import bypass_driver, create_driver
from utils import time_cal, pinger, ipchanger, alarm
from clicks import clk, search
import time

@time_cal
@alarm(timer=60)
def test_alpha():
    #ipchanger()
    #pinger()
    driver = bypass_driver()
    short_url = "https://urllinkshort.in/3OL3"
    search(driver, short_url, text_to_find="network", max_retries=101)
    clk(driver, "suntechu.in", method="partial_link_text")
    print("t1")
    clk(driver, "CloseAd", method="id", click_method="js", time=5, show_error=False)
    print("t2")
    clk(driver, "Dual Tap Fast", method="partial_link_text", click_method="js", time=20)
    print("t3")
    clk(driver, '#rtg7', method="css_selector", time=5, click_method="action_chains")
    print("t4")
    clk(driver, "CloseAd", method="id", click_method="js", time=5, show_error=False)
    print("t5")
    clk(driver, '#rtg-generate > center > button', method="css_selector", click_method="js", time=20)
    print("t6")
    clk(driver, "#rtg-snp2", method="css_selector", click_method="js", time=20)
    print("t7")
    clk(driver, "CloseAd", method="id", click_method="js", time=5, show_error=False)
    print("t8")
    clk(driver, "body > section > div > div > div > div > div:nth-child(3) > a", method="css_selector", wait_click=1)
    print("t9")
    time.sleep(1)
    driver.quit()





while True:
    try:
        test_alpha()  # Call the function test_alpha()
    except Exception as e:
        print(f"Error occurred: {e}")
        continue  # If an error occurs, continue to the next iteration to rerun the function
