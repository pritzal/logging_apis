import requests
import json
import os  # Import os to handle directory creation

# Base URL for your FastAPI application
BASE_URL = "http://localhost:8000"

# Test data for logging an exception
test_data_exception = {
    "application_name": "TestApp",
    "application_type": "Web",
    "category": "Error",
    "message": "Test Null reference exception",
    "stack_trace": "at TestApp.Program.Main() in Program.cs:line 14",
    "exception_details": "System.NullReferenceException: Object reference not set to an instance of an object.",
    "exp_object": "Test Main Program",
    "exp_process": "Test Initialization",
    "inner_exception": "None"
}

# Ensure the directory exists
def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Test function to log an exception using POST request
def log_exception():
    response = requests.post(f"{BASE_URL}/save-application-exception/", json=test_data_exception)
    print(f"Log Exception Response: {response.json()}")

    # Ensure the directory exists
    ensure_directory_exists("test_data")

    # Save response to a file
    with open("test_data/application_logs.json", "w") as log_file:
        json.dump(response.json(), log_file, indent=4)

# Test function to fetch exceptions using GET request
def fetch_exceptions():
    params = {"type": "Error", "application_id": 1}
    response = requests.get(f"{BASE_URL}/get-application-exceptions/", params=params)
    print(f"Fetch Exceptions Response: {response.json()}")

    # Ensure the directory exists
    ensure_directory_exists("test_data")

    # Save response to a file
    with open("test_data/fetched_exceptions.json", "w") as fetch_file:
        json.dump(response.json(), fetch_file, indent=4)

# Test function to fetch application details using GET request
def fetch_application_details():
    params = {"app_id": 1}
    response = requests.get(f"{BASE_URL}/get-application-details/", params=params)
    print(f"Fetch Application Details Response: {response.json()}")

    # Ensure the directory exists
    ensure_directory_exists("test_data")

    # Save response to a file
    with open("test_data/application_details.json", "w") as details_file:
        json.dump(response.json(), details_file, indent=4)

if __name__ == "__main__":
    log_exception()
    fetch_exceptions()
    fetch_application_details()
