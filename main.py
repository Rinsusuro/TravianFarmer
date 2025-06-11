from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# === CONFIG ===
website_url = "https://ts7.x1.international.travian.com/dorf1.php"  # Replace with your desired URL

# === Setup Chrome Options ===
chrome_options = Options()
chrome_options.headless = False  # Ensure it's not headless
chrome_options.add_argument("--start-maximized")  # Optional: start maximized

# === Initialize WebDriver ===
driver = webdriver.Chrome(options=chrome_options)

# === Open Website ===
driver.get(website_url)

# === Optional: Keep it open for a while before closing ===
time.sleep(10)  # seconds

# === Cleanup ===
driver.quit()
