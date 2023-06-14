import statistics
import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service


# Function to measure the response time of a route
def measure_response_time(url):
    options = FirefoxOptions()
    options.set_preference("media.autoplay.default", 0)
    options.set_preference("media.autoplay.allow-muted", True)
    options.add_argument("-headless")  # Run Firefox in headless mode (optional)

    # Set the path to the Firefox driver executable
    firefox_driver_path = r"C:\Users\Loukas Melissopoulos\Documents\PythonProjekte\FlaskVideo"

    driver = webdriver.Firefox(service=Service(firefox_driver_path), options=options)

    start_time = time.time()
    driver.get(url)
    end_time = time.time()

    driver.quit()

    response_time = (end_time - start_time) * 1000  # Convert to milliseconds
    return response_time


# Function to run the load testing
def run_load_testing(routes, num_users, num_requests):
    response_times = []

    for _ in range(num_users):
        user_times = []
        for _ in range(num_requests):
            for route in routes:
                response_time = measure_response_time(route)
                user_times.append(response_time)
        response_times.append(user_times)

    return response_times


if __name__ == '__main__':
    routes = ['http://localhost:5000/video', 'http://localhost:5000/video_buff', 'http://localhost:5000/video_comp']
    num_users = 100
    num_requests = 10

    # Run the load testing
    response_times = run_load_testing(routes, num_users, num_requests)

    # Calculate statistics
    for i, route in enumerate(routes):
        times = []
        for user_times in response_times:
            times.extend(user_times[i::len(routes)])  # Get response times for the specific route

        print(f"Statistics for route '{route}':")
        print(f"  Average Response Time: {statistics.mean(times):.2f} ms")
        print(f"  Minimum Response Time: {min(times):.2f} ms")
        print(f"  Maximum Response Time: {max(times):.2f} ms")
        print(f"  Standard Deviation: {statistics.stdev(times):.2f} ms")
