from selenium import webdriver

def before_all(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(0.5)

def after_all(context):
    context.driver.quit()