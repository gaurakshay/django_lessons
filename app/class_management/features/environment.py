from splinter.browser import Browser


def before_all(context):
    context.browser = Browser('firefox')


def after_all(context):
    context.browser.quit()
    context.browser = None

# from toolkit.helpers.bdd import flush_context, save_failure_screenshot, setup_test_environment
#
# from utils.bdd_test_helpers import create_users, load_fixtures
#
#
# def before_scenario(context, scenario):  # The scenario param is used behind the scenes
#     setup_test_environment(context, scenario)
#     create_users()
#     load_fixtures()
#
#
# def after_step(context, step):
#     save_failure_screenshot(context, step)
#
#
# def after_scenario(context, scenario):
#     flush_context(context, scenario)
