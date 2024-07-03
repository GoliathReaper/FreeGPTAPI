from selenium.webdriver.firefox.service import Service
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

##############  Setting up Chatgpt
QUESTION = "which is better chat-gpt-3 vs chat-gpt-4o" # ADD YOUR QUESTION HERE
CHAT_GPT_URL = "" # ADD YOUR CHAT URL HERE
##############

##################################  Setting up Geckodriver
# Specify the path to the geckodriver executable
driver_path = "C:\\Users\\Goliath PC\\PycharmProjects\\chatGPT_FREE_API\\geckodriver.exe"
# Specify the path to the Firefox binary (if needed)
binary = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
# Specify the path to the Firefox profile
profile_path = "C:\\Users\\Goliath PC\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\rdbzyx7b.default-release\\"
###################################

service = Service(driver_path)

# Use FirefoxOptions to set the binary location
options = Options()
options.binary_location = binary

# Run Firefox in Headless mode
options.add_argument('--headless')  # Run in headless mode

# Create a FirefoxProfile object with the profile path
profile = FirefoxProfile(profile_path)

# Add the FirefoxProfile to the Options object
options.profile = profile

# Initialize the Firefox WebDriver with the Service, Options, and Profile objects
driver = webdriver.Firefox(service=service, options=options)

driver.get(CHAT_GPT_URL)

wait = WebDriverWait(driver, 10)

time.sleep(3)
# Check if the element exists
textarea = driver.find_element(By.ID, 'prompt-textarea')

# Add text to the textarea
textarea.send_keys(QUESTION)

time.sleep(3)

button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="fruitjuice-send-button"]')

button.click()

time.sleep(20)

# Find the element using XPath
# element = driver.find_element_by_xpath('//div[@data-scroll-anchor="true"]')
# element = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@data-scroll-anchor="true"]')))
#
# # Extract the text
# text = element.text
#
# print(text)


element = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@data-scroll-anchor="true"]')))

# Extract the text
text = element.text

print(text)

# time.sleep(10)

# Close the browser
driver.quit()
