from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Search for {product}')
def search_product(context, product):
    # find search field and enter text
    context.driver.find_element(By.ID, 'search').send_keys(product)
    # click search
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    # wait for the page with search results to load
    sleep(6)


@then('Verify search worked for {product}')
def verify_search_results(context, product):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert product in actual_text, f'Expected {product} is not in actual text {actual_text}'

    print('Text case passed')

@then('Verify correct url is displayed for {product}')
def verify_url(context, product):
    url = context.driver.current_url
    assert product in url, f'Expected {product} is not in current {url}'

    print('Text case passed')

# -----------------------------------------------------------------------------------------------------

@when('Click on cart icon')
def click_cart_icon(context):
    # find target cart icon and click on it
    context.driver.find_element(By.XPATH, "//a[@data-test='@web/CartLink']").click()
    # wait for the page to load
    sleep(6)


@then('Verify correct message is shown')
def verify_message(context):
    # verify
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.XPATH, "//h1[@class='sc-fe064f5c-0 dtCtuk']").text
    print(actual_text)
    assert expected_text in actual_text, f'Expected {expected_text} is not in actual text {actual_text}'
    print('Text case passed')

# -------------------------------------------------------------------------------------------------------

@when('Click sign in button')
def click_sign_in_button(context):
    # click sign in button on the right side of the page (part 1)
    context.driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()
    # wait for the page to load
    sleep(6)

@when('Click sign in button additional step')
def click_sign_in_button_additional_step(context):
    # click sign in button on the right side of the page (part 1)
    context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
    # wait for the page to load
    sleep(6)

@then('Verify sign in form is shown')
def verify_sign_in_form_message(context):
    # verify
    expected_text = 'Sign into your Target account'
    actual_text = context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
    print(actual_text)
    assert expected_text in actual_text, f'Expected {expected_text} is not in actual text {actual_text}'
    print('Text case passed')

