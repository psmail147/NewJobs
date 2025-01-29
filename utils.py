from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def get_driver(profile_path, profile_name, driver_path):
    options = webdriver.ChromeOptions()
    options.add_argument(f"--user-data-dir={profile_path}")
    options.add_argument(f"--profile-directory={profile_name}")
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    return driver