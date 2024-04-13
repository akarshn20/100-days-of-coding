from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time


def abort_application():
    close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)
    discard_button = driver.find_element(By.CLASS_NAME, "artdeco-button--secondary")
    discard_button.click()


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(
    "https://www.linkedin.com/jobs/search/?currentJobId=3586148395&f_"
    "LF=f_AL&geoId=101356765&location=London%2C%20England%2C%20United%20Kingdom&refresh=true"
)

# time.sleep(2)
# reject_button = driver.find_element(by=By.CSS_SELECTOR, value='button[action-type="DENY"]')
# reject_button.click()

time.sleep(2)
sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

time.sleep(5)
email_field = driver.find_element(By.ID, "username")
email_field.send_keys("Your Email ID")
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("Your Password")
password_field.send_keys(Keys.ENTER)

time.sleep(3)
all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

for listing in all_listings:
    print("Opening Listing")
    listing.click()
    time.sleep(2)
    try:
        easy_apply_button = driver.find_element(By.CLASS_NAME, "jobs-apply-button--top-card")
        easy_apply_button.click()

        button = driver.find_element(By.XPATH, '//button[contains(@class, "artdeco-button--primary")]')
        if button.text == "Next":
            abort_application()
            print("Complex Application")
            continue
        else:
            button.click()

        time.sleep(2)
        close = driver.find_element(By.CSS_SELECTOR, "artdeco-modal__dismiss")
        close.click()

    except NoSuchElementException:
        abort_application()
        print("No application button, skipped")
        continue

time.sleep(3)
driver.quit()


