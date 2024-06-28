# Amazon Logo (find by XPATH)
# driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")
#
# Amazon Email Field (find by ID)
# driver.find_element(By.ID, 'ap_email')
#
# Amazon Continue Button (find by ID)
# driver.find_element(By.ID, 'continue')
#
# Amazon Conditions Of Use Link (find by XPATH)
# driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088']")
#
# Amazon Privacy Notice Link (find by XPATH)
# driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_privacy_notice?ie=UTF8&nodeId=468496']")
#
# Amazon Need Help Link (find by XPATH)
# driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")
#
# Amazon Forgot Your Password Link (find by ID)
# driver.find_element(By.ID, 'auth-fpp-link-bottom')
#
# Amazon Other Issues With Sign-In Link (find by ID)
# driver.find_element(By.ID, 'ap-other-signin-issues-link')
#
# Amazon Create Your Account Button (find by ID)
# driver.find_element(By.ID, 'createAccountSubmit')

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')

sleep(6)

# click sign in button on the right side of the page (part 1)
driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()

sleep(6)

# click sign in button on the right side of the page (part 2)
driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()

sleep(6)

# verify "Sign into your Target account" text is shown
expected_text = 'Sign into your Target account'
actual_text = driver.find_element(By.XPATH, "//h1[@class='styles__StyledHeading-sc-1awz1yh-0 styles__AuthHeading-sc-kz6dq2-2 gfuwhI kcHdEa']").text
print(actual_text)
assert expected_text in actual_text, f'Expected {expected_text} is not in actual text {actual_text}'

sleep(10)

print('Text case passed')
sleep(6)

# verify "SignIn" button is shown
driver.find_element(By.ID, 'login')

sleep(10)