#utils.py 



# user agent generator
def generate_random_user_agent():
    import random
    os_list = [
        "Windows NT 10.0", 
        "Macintosh; Intel Mac OS X 10_15", 
        "X11; Linux x86_64", 
        "Android 12", 
        "Android 12",  # Extra for more Android results
        "iOS 16.0"
    ]
    browser_list = ["Chrome", "Firefox", "Safari", "Edge"]
    phone_arches = ["ARMv8", "x86_64"] 
    phone_models = ["iPhone 13", "Samsung Galaxy S22", "Google Pixel 6"]

    def random_android_version():
        return random.randint(10, 12)  

    def random_version(max_major=105, max_minor=3):
        return f"{random.randint(80, max_major)}.{random.randint(0, max_minor)}.{random.randint(0, 9999)}"

    os_choice = random.choice(os_list)
    browser_name = random.choice(browser_list)
    browser_version = random_version()

    if os_choice in ["Android 12"]: 
        arch = random.choice(phone_arches)
        model = random.choice(phone_models)
        android_version = random_android_version()
        user_agent = f"Mozilla/5.0 (Android {android_version}; {arch}) AppleWebKit/537.36 (KHTML, like Gecko) {browser_name}/({model}) {browser_version}"
    else:  
        user_agent = f"Mozilla/5.0 ({os_choice}) AppleWebKit/537.36 (KHTML, like Gecko) {browser_name}/{browser_version}"

    return user_agent
    
# Example usage
# random_user_agent = generate_random_user_agent()
# print(random_user_agent)


# time decorator
def time_cal(func):
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of {func.__name__}: {end_time - start_time} seconds")
        return result
    return wrapper

# How to use
# @time_cal
# def anyfunc():


# ip changer 


def ipchanger():
    import time
    import os

    os.system("adb shell cmd connectivity airplane-mode enable")
    time.sleep(4)
    os.system("adb shell cmd connectivity airplane-mode disable")
    #os.system("systemd-resolve --flush-caches")

# Call the function to change ip
# ipchanger()
    

# pinger 
@time_cal
def pinger():
    from ping3 import ping
    import time
    import os

    while True:
        # Attempt to ping google.com
        response = ping("google.com")

        # Check if the ping was successful
        if response is not None:
            print("Ping successful!")
            #os.system("systemd-resolve --flush-caches")
            break  # Exit the loop upon successful ping
        else:
            #print("Ping unsuccessful. Retrying...")
            # Add a delay before retrying to prevent excessive attempts
            time.sleep(1)  # You need to import time module for this line

# Call the function to start pinging
# pinger()




# multiprocessing
import threading
import sys

class TimeoutThread(threading.Thread):
    def __init__(self, target, args=(), kwargs={}, time_limit=None):
        super().__init__()
        self.target = target
        self.args = args
        self.kwargs = kwargs
        self.time_limit = time_limit
        self.result = None
        self.error = None

    def run(self):
        try:
            if self.time_limit is None:
                self.result = self.target(*self.args, **self.kwargs)
            else:
                self.timer = threading.Timer(self.time_limit, self.handle_timeout)
                self.timer.start()
                self.result = self.target(*self.args, **self.kwargs)
                self.timer.cancel()
        except Exception as e:
            self.error = e

    def handle_timeout(self):
        # If the function does not complete within the time limit, raise an exception to halt execution
        raise TimeoutError("Function execution timed out")

def threader(func, time_limit=None, args=(), kwargs={}):
    thread = TimeoutThread(target=func, args=args, kwargs=kwargs, time_limit=time_limit)
    thread.start()
    thread.join()  # Wait for the thread to finish
    if thread.error:
        raise thread.error
    return thread.result

