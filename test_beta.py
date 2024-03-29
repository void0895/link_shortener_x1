# Test beta

from driver_instance import bypass_driver, create_driver
from utils import time_cal, pinger, ipchanger, alarm, captcha_solve
from clicks import clk, search
import time
from recap2 import recaptcha

@alarm(timer=60)
@time_cal
def test_beta():
    driver = bypass_driver()
    short_url = "https://adcorto.com/eWKLTFjOF2jrJ9aKK"
    search(driver, short_url, text_to_find="network", max_retries=10)
    clk(driver, "#close-btn > svg > path", method="css_selector", click_method="js", wait_click=1, time=30)
    print("done")
    time.sleep(15)
    #ecaptcha(driver)
    time.sleep(60)





test_beta()
#close-btn > svg > path