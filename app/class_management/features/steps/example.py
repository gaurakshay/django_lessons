from behave import *


# @given('we have behave installed')
# def step_impl(context):
#     pass
#
#
# @when('we implement a test')
# def step_impl(context):
#     assert True is not False
#
#
# @when('we implement another test')
# def step_impl(context):
#     assert True is not False
#
#
# @then('behave will test it for us')
# def step_impl(context):
#     assert context.failed is False


@given('I am on the department add page')
def step_impl(context):
    browser = context.browser
    browser.visit('http://127.0.0.1:8000/mgmt/dept/add')
    print(browser.is_text_present)
    assert (browser.is_text_present is True), "Page doesn't exist."


@when('I click add button')
def step_impl(context):
    browser = context.browser
    browser.find_by_id('addBtn').first.click()


@step('I enter valid data')
def step_impl(context):
    pass


@then('I should see a success message')
def step_impl(context):
    pass
