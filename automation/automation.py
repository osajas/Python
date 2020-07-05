from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')


chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome_browser.title

button_text = chrome_browser.find_element_by_class_name('btn-default')

button_shape = chrome_browser.find_element_by_css_selector('#get-input > .btn')
print(button_shape)
print(button_text.get_attribute('innerHTML'))

user_message = chrome_browser.find_element_by_id("user-message")

user_message.clear()
user_message.send_keys("Hey there")
button_text.click()
output_message = chrome_browser.find_element_by_id('display')
assert 'Hey there' in output_message.text
chrome_browser.close()