import concurrent.futures
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service


# Define the function to simulate user actions and collect statistics
def simulate_user_action(driver):
    start_time = time.time()

    try:
        # Perform the desired actions on your Flask app
        driver.get("http://127.0.0.1:5000")  # Replace with the URL of your Flask app
        # Add more actions if needed (e.g., form submissions, button clicks, etc.)

        # Print the title of the page for demonstration
        # print(f"Request #{request_number}: {driver.title}")

    finally:
        # Calculate the elapsed time
        end_time = time.time()
        elapsed_time = end_time - start_time

        # Return the elapsed time
        return elapsed_time


# Define the number of concurrent users
concurrent_users = 100

# Set additional options for the Firefox driver
firefox_options = Options()
firefox_options.set_preference("media.autoplay.default", 0)
firefox_options.set_preference("media.autoplay.allow-muted", True)
firefox_options.add_argument("-headless")  # Run Firefox in headless mode (optional)

# Set the path to the Firefox driver executable
firefox_driver_path = r"C:\\Users\Loukas\Desktop\Python\FlaskVideo"  # Replace with the actual path to geckodriver

# Initialize the Firefox WebDriver
driver = webdriver.Firefox(service=Service(firefox_driver_path), options=firefox_options)

try:
    # Create a concurrent execution pool
    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrent_users) as executor:
        # Submit the user action function to the executor
        futures = [executor.submit(simulate_user_action, driver) for _ in range(1000)]

        # Wait for all tasks to complete
        for future in concurrent.futures.as_completed(futures):
            future.result()

    # Collect statistics from the completed tasks
    elapsed_times = [future.result() for future in futures]

    # Calculate statistics
    total_requests = len(elapsed_times)
    total_time = sum(elapsed_times)
    average_time = total_time / total_requests
    min_time = min(elapsed_times)
    max_time = max(elapsed_times)

    # Print the statistics
    print("Total Requests: ", total_requests)
    print("Total Time: ", total_time)
    print("Average Time: ", average_time)
    print("Min Time: ", min_time)
    print("Max Time: ", max_time)

finally:
    # Close the WebDriver session
    driver.quit()
