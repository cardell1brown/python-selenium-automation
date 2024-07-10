# Amazon Logo (find by CSS + Class)
# driver.find_element(By.CSS_SELECTOR, ".a-icon.a-icon-logo")

# Create account (find by CSS + Class)
# driver.find_element(By.CSS_SELECTOR, "div.a-section.a-spacing-small.a-text-center.a-size-mini")

# Your name (find by CSS)
# driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")

# Mobile number or email (find by CSS)
# driver.find_element(By.CSS_SELECTOR, "#ap_email")

# Password (find by CSS)
# driver.find_element(By.CSS_SELECTOR, "#ap_password")

# Re-enter password (find by CSS)
# driver.find_element(By.CSS_SELECTOR, "#ap_password_check")

# Continue button (find by CSS)
# driver.find_element(By.CSS_SELECTOR, "#continue")

# Conditions of Use (find by XPATH)
# driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088']")

# Privacy Notice (find by XPATH)
# driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice?ie=UTF8&nodeId=468496']")

# Created by rocco at 7/7/2024
Feature: Target shopping cart message
  # Enter feature description here

  Scenario: Validate that the "Your cart is empty" message is shown
    Given Open target main page
    When Click on cart icon
    Then Verify correct message is shown

  Scenario: Validate that a logged out user can sign in
    Given Open target main page
    When Click sign in button
    When Click sign in button additional step
    Then Verify sign in form is shown