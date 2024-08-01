from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target circle page')
def open_target(context):
    context.driver.get('https://www.target.com/circle')
    sleep(6)


# @then('Verify {number} benefit cells are present')
# def verify_amount_of_benefit_cells(context, number):
#     number = int(number)
#     links = context.driver.find_elements(By.XPATH, "//div[@class='cell-item-content']").text
#     assert len(links) == number, f'Expected {number} links but got {len(links)}'


@then('Verify 10 benefit cells are present')
def verify_amount_of_benefit_cells(context):
    links = context.driver.find_elements(By.XPATH, "//div[@class='cell-item-content']")
    assert len(links) == 10, f'Expected 10 benefit cells but got {len(links)}'