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
    time.sleep(5)
    os.system("adb shell cmd conenctivity airplane-mode disable")

# Call the function to change ip
# ipchanger()
    

# pinger 
def pinger():
    from ping3 import ping

    while True:
        # Attempt to ping google.com
        response = ping("google.com")

        # Check if the ping was successful
        if response is not None:
            print("Ping successful!")
            break  # Exit the loop upon successful ping
        else:
            #print("Ping unsuccessful. Retrying...")
            # Add a delay before retrying to prevent excessive attempts
            time.sleep(1)  # You need to import time module for this line

# Call the function to start pinging
# pinger()




# multiprocessing
@time_cal
def parallel(*funcs, time_limit=5, lock=True):
    import multiprocessing
    import time
    """
    Run given functions in parallel with multiprocessing.
    
    Args:
        *funcs: Variable length list of functions to run in parallel.
        time_limit (int): The maximum time in seconds for each function to run (default: 60).
        lock (bool): Whether to lock all multiprocessing functions to wait for others (default: True).
    """
    processes = []
    start_time = time.time()

    for func in funcs:
        p = multiprocessing.Process(target=func)
        processes.append(p)
        p.start()

        if lock:
            p.join()

        # Check if the maximum time limit has been exceeded
        if time.time() - start_time == time_limit:
            print("Time limit reached. Stopping further processes.")
            break

    # Wait for all processes to finish if not locked
    if not lock:
        for p in processes:
            p.join()

# Example functions:
#def myfunc():
    #print("Function 1 called.")
    #time.sleep(2)  # Simulate some processing time
#def myfunc2():
    #print("Function 2 called.")
    #time.sleep(1)  # Simulate some processing time
# Example usage:
#run_parallel_functions(myfunc, myfunc2, time_limit=5, lock=True)
