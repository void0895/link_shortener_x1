#clicks.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils import time_cal

@time_cal
def clk(driver, locator, method="xpath", click_method="click", show_error=True, time=10):
    """
    Find and optionally click a web element based on the specified locating strategy and clicking method.

    Parameters:
        driver: WebDriver instance.
        locator: The locator value (e.g., XPath, ID, class name).
        method: The locating strategy to use (default is "xpath").
        click_method: The clicking method to use (default is "click"). Set to 0 to only find the element.
        show_error: Whether to print error messages (default is True).
        time: Maximum time to wait for the element to be located (default is 10 seconds).

    Returns:
        The located WebElement object if found and clicked successfully, None otherwise.
    """
    try:
        wait = WebDriverWait(driver, time)
        if method.lower() == "id":
            element = wait.until(EC.presence_of_element_located((By.ID, locator)))
        elif method.lower() == "class":
            element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, locator)))
        elif method.lower() == "name":
            element = wait.until(EC.presence_of_element_located((By.NAME, locator)))
        elif method.lower() == "link_text":
            element = wait.until(EC.presence_of_element_located((By.LINK_TEXT, locator)))
        elif method.lower() == "partial_link_text":
            element = wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, locator)))
        elif method.lower() == "tag_name":
            element = wait.until(EC.presence_of_element_located((By.TAG_NAME, locator)))
        elif method.lower() == "css_selector":
            element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)))
        else:  # Default to XPath
            element = wait.until(EC.presence_of_element_located((By.XPATH, locator)))
        
        if click_method == 0:
            return element
        
        if click_method.lower() == "js":
            driver.execute_script("arguments[0].click();", element)
        elif click_method.lower() == "action_chains":
            from selenium.webdriver.common.action_chains import ActionChains
            ActionChains(driver).move_to_element(element).click().perform()
        elif click_method.lower() == "send_keys":
            element.send_keys(Keys.RETURN)
        elif click_method.lower() == "javascript_click":
            driver.execute_script("arguments[0].dispatchEvent(new Event('click'));", element)
        else:
            element.click()
        return element
    except Exception as e:
        if show_error:
            print(f"An error occurred: {e}")
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


