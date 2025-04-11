from selenium import webdriver

def before_scenario(context, scenario):
    context.driver.delete_all_cookies()
    
def before_all(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)

def after_all(context):
    context.driver.quit()