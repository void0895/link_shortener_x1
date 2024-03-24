# Test alpha

from driver_instance import bypass_driver, create_driver
from utils import time_cal, pinger, ipchanger, parallel
from clicks import clk
import time 

@time_cal
def test_alpha():
    #ipchanger()
    pinger()
    driver = create_driver()
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
    clk(driver, "body > section > div > div > div > div > div:nth-child(3) > a", method="css_selector", wait_click=1)
    print("t9")
    time.sleep(1)
    driver.quit()

test_alpha()


