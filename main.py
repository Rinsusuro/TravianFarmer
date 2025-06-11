from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# === Credentials & URL ===
email = "your_email@example.com"
password = "your_secure_password"
website_url = "https://ts7.x1.international.travian.com/"  # Replace with actual login page

# === Chrome Options ===
options = Options()
options.headless = False  # Show browser
options.add_argument("--start-maximized")

# === Start Chrome WebDriver ===
driver = webdriver.Chrome(options=options)

try:
    # Open the target website
    driver.get(website_url)

    # Wait until the form inputs are loaded
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "name")))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))

    # Fill in email and password
    driver.find_element(By.NAME, "name").send_keys(email)
    driver.find_element(By.NAME, "password").send_keys(password)

    # Click the submit button
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    submit_button.click()

except Exception as e:
    print(f"Error: {e}")
finally:
    pass  # You can add driver.quit() here if you want to close after login
