from selenium import webdriver
import chromedriver_autoinstaller
from bs4 import BeautifulSoup
import time
import requests
import pandas as pd

# Automatically download and install the correct version of ChromeDriver
chromedriver_autoinstaller.install()

# Initialize Selenium WebDriver
driver = webdriver.Chrome()

# Maximize the browser window
driver.maximize_window()

# Set a default wait time
driver.implicitly_wait(10)

# Load the webpage
url = "https://www.inmotionhosting.com/"
driver.get(url)

# Optional: wait for the page to load completely
time.sleep(5)

# Extract page content
page_content = driver.page_source

# Parse the page content using BeautifulSoup
soup = BeautifulSoup(page_content, "html.parser")

# Identify elements containing hosting plan details
# Example: Assuming plans are in a div with class 'plan-details'
plans = soup.find_all('div', class_='plan-details')

# Create lists to store the extracted data
plan_names = []
plan_features = []
plan_pricing = []

# Loop through the identified elements and extract data
for plan in plans:
    # Extract plan name
    name = plan.find('h3').text.strip()
    plan_names.append(name)

    # Extract plan features
    features = plan.find('ul', class_='features').text.strip()
    plan_features.append(features)

    # Extract plan pricing
    price = plan.find('span', class_='price').text.strip()
    plan_pricing.append(price)

# Create a DataFrame to store the extracted data
data = pd.DataFrame({
    'Plan Name': plan_names,
    'Features': plan_features,
    'Pricing': plan_pricing
})

# Save the DataFrame to a CSV file
data.to_csv('hosting_plans.csv', index=False)

print("Data saved to hosting_plans.csv")

# Close the Selenium WebDriver
driver.quit()