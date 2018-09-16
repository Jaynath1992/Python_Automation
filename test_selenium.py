from selenium import webdriver
from time import sleep as wait
from selenium.webdriver.chrome.options import Options


class TestSelenium(object):

    def test_launch_browser(self):
	options = Options()
        options.add_argument("--disable-infobars")  #disable info bars in browser("Chrome is being controlled by automated test software")
        options.add_argument("test-type")  # solve the chrome security warning
	options.add_argument("--acceptInsecureCerts=true")
	options.add_argument('headless')
        options.add_argument("--window-size=1325x744")
	options.add_argument('disable-gpu')
	options.add_argument('no-sandbox')
        browser = webdriver.Chrome(chrome_options=options)
        browser.get('https://s-composer.vrli.com/')
        browser.maximize_window()
        browser.implicitly_wait(30)
        print browser.title
        browser.find_element_by_id('username').send_keys('jaynath.kumar@nuance.com')
        browser.find_element_by_id('password').send_keys('JayPatel#125') 
	browser.find_element_by_id('kc-login').click()       
	wait(30)
        assert browser.find_element_id("logo").is_displayed() == True
        print browser.title

