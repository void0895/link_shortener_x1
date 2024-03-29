#clicks.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from utils import time_cal
import time, sys



class element_enabled(object):
    """
    An expectation for checking that an element is enabled.
    
    Parameters:
        locator (tuple): The locator used to find the element (e.g., By.ID, "id").
    """
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        element = driver.find_element(*self.locator)
        return element.is_enabled() and "disabled" not in element.get_attribute("class")
        
@time_cal
def clk(driver, locator, method="xpath", click_method="click", wait_click=0, show_error=True, time=10, send_keys_value=None):
    """
    Find and optionally click a web element based on the specified locating strategy and clicking method.

    Parameters:
        driver: WebDriver instance.
        locator: The locator value (e.g., XPath, ID, class name).
        method: The locating strategy to use (default is "xpath").
        click_method: The clicking method to use (default is "click"). Set to 0 to only find the element.
        wait_click: Whether to wait for the element to be clickable before clicking (default is 0, which means off).
        show_error: Whether to print error messages (default is True).
        time: Maximum time to wait for the element to be located (default is 10 seconds).
        send_keys_value: The text to send if using the 'send_keys' click method (default is None).

    Returns:
        The located WebElement object if found and clicked successfully, None otherwise.
    """
    try:
        wait = WebDriverWait(driver, time)
        if method.lower() == "id":
            locator_method = By.ID
        elif method.lower() == "class":
            locator_method = By.CLASS_NAME
        elif method.lower() == "name":
            locator_method = By.NAME
        elif method.lower() == "link_text":
            locator_method = By.LINK_TEXT
        elif method.lower() == "partial_link_text":
            locator_method = By.PARTIAL_LINK_TEXT
        elif method.lower() == "tag_name":
            locator_method = By.TAG_NAME
        elif method.lower() == "css_selector":
            locator_method = By.CSS_SELECTOR
        else:  # Default to XPath
            locator_method = By.XPATH
        
        element = wait.until(EC.presence_of_element_located((locator_method, locator)))
        
        if click_method == 0:
            return element
        
        if wait_click == 1:
            # Wait for the element to be clickable
            wait.until(EC.element_to_be_clickable((locator_method, locator)))

        if wait_click == 1:
            # Wait until the element is enabled
            wait.until(element_enabled((locator_method, locator)))

        if click_method.lower() == "js":
            driver.execute_script("arguments[0].click();", element)
        elif click_method.lower() == "action_chains":
            ActionChains(driver).move_to_element(element).click().perform()
        elif click_method.lower() == "send_keys":
            element.send_keys(send_keys_value)  # Send keys provided in send_keys_value
        elif click_method.lower() == "javascript_click":
            driver.execute_script("arguments[0].dispatchEvent(new Event('click'));", element)
        else:
            element.click()
        
        return element
    except Exception as e:
        if show_error:
            driver.quit()
            raise Exception("Error from clk!. Locator-", locator)
        return None



# Usage examples:
# element = clk(driver, "myButton", method="id", click_method=0)
# clk(driver, "myButton", method="id", click_method=0, show_error=True)
# if element:
#     element.click()

# Note 
# default 
# driver - "driver" instance if not mentioned
# method - xpath
# click_method -  normal click
# time - 10s
# show_error - True 


def search(driver, url, text_to_find=None, max_retries=3, retry_delay=2):
    retries = 0
    while retries < max_retries:
        try:
            #driver.get(url)
            driver.execute_script("window.location.href = '{}';".format(url))
            if text_to_find is None:
                return
            elif text_to_find in driver.page_source:
                retries += 1
                time.sleep(retry_delay)
            else:
                return
        except NoSuchElementException:
            retries += 1
            time.sleep(retry_delay)
        except WebDriverException as e:
            error_message = str(e)
            if "net::ERR_NAME_NOT_RESOLVED" in error_message or "net::ERR_ADDRESS_UNREACHABLE" in error_message:
                retries += 1
                time.sleep(retry_delay)
            else:
                driver.quit()
                raise Exception("Webdriver related error!")  # Reraise other WebDriverExceptions
        
        




