from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# === Credentials & URL ===
email = "placeholder user"
password = "placeholder password"
website_url = "https://ts7.x1.international.travian.com/"  # Replace with actual login page

# === Chrome Options ===
options = Options()
options.headless = True  # Show browser
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

    # Wait for link to appear after login
    target_href = "https://ts7.x1.international.travian.com/build.php?id=39&gid=16"
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, f'a[href="{target_href}"]'))
    ).click()

    # === [3] CLICK FIRST START FARM LIST BUTTON ===
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "startFarmList"))
    ).click()

    print("Script complete. Browser will remain open for manual inspection.")
    input("Press Enter to exit the script and close the browser...")

except Exception as e:
    print(f"Error: {e}")
finally:
    pass  # You can add driver.quit() here if you want to close after login
