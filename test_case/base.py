#!/usr/bin/python
# -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

from config import Config


class Ebao(object):
    def __init__(self, browser='firefox'):
        if browser == "firefox":
            ua = 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_1 like Mac OS X) \
            AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A403 \
            MicroMessenger/6.3.27 NetType/WIFI Language/zh_CN'
            webdriver.FirefoxProfile().set_preference('general.useragent.override', ua)
            opts = Options()
            opts.headless = True
            driver = webdriver.Firefox(options = opts)

        elif browser == "chrome":
            driver = webdriver.Chrome(chrome_options=Config.CHROME_USER_AGENT)
        elif browser == "ie":
            driver = webdriver.Ie()
        elif browser == "phantomjs":
            driver = webdriver.PhantomJS()
        try:
            self.driver = driver
        except Exception:
            raise NameError("Not found this browser,You can enter 'firefox', 'chrome', 'ie' or 'phantomjs'.")

    def get(self, url):
        self.driver.get(url)

    def max_window(self):
        """
        Set browser window maximized.

        Usage:
        driver.max_window()
        """
        self.driver.maximize_window()

    def set_window_size(self, wide, high):
        """
        Set browser window wide and high.

        Usage:
        driver.set_window_size(wide,high)
        """
        self.driver.set_window_size(wide, high)

    def wait(self, seconds):
        """
        Implicitly wait.All elements on the page.

        Usage:
        driver.wait(10)
        """
        self.driver.implicitly_wait(seconds)

    def find_element(self, element):
        """
        Judge element positioning way, and returns the element.

        Usage:
        driver.find_element("id=kw")
        """
        if "=" not in element:
            raise NameError("SyntaxError: invalid syntax, lack of '='.")

        by = element.split("=")[0]
        value = element.split("=")[1]

        if by == "id":
            return self.driver.find_element_by_id(value)
        elif by == "name":
            return self.driver.find_element_by_name(value)
        elif by == "class":
            return self.driver.find_element_by_class_name(value)
        elif by == "text":
            return self.driver.find_element_by_link_text(value)
        elif by == "text_part":
            return self.driver.find_element_by_partial_link_text(value)
        elif by == "xpath":
            return self.driver.find_element_by_xpath(value)
        elif by == "css":
            return self.driver.find_element_by_css_selector(value)

        else:
            raise NameError("Please enter the correct targeting elements,'id','name','class','text','xpath','css'.")

    def find_by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    def find_by_classes(self, name):
        return self.driver.find_elements_by_class_name(name)

    def wait_element(self, element, seconds=5):
        """
        Waiting for an element to display.

        Usage:
        driver.wait_element("id=kw",10)
        """
        if "=" not in element:
            raise NameError("SyntaxError: invalid syntax, lack of '='.")

        by = element.split("=")[0]
        value = element.split("=")[1]

        if by == "id":
            WebDriverWait(self.driver, seconds, 0.5).until(EC.presence_of_element_located((By.ID, value)))
        elif by == "name":
            WebDriverWait(self.driver, seconds, 0.5).until(EC.presence_of_element_located((By.NAME, value)))
        elif by == "class":
            WebDriverWait(self.driver, seconds, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, value)))
        elif by == "text":
            WebDriverWait(self.driver, seconds, 0.5).until(EC.presence_of_element_located((By.LINK_TEXT, value)))
        elif by == "xpath":
            WebDriverWait(self.driver, seconds, 0.5).until(EC.presence_of_element_located((By.XPATH, value)))
        elif by == "css":
            WebDriverWait(self.driver, seconds, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)))
        else:
            raise NameError("Please enter the correct targeting elements,'id','name','class','text','xpaht','css'.")

    def send_keys(self, element, text):
        """
        Operation input content after clear.

        Usage:
        driver.send_keys("id=kw","selenium")
        """
        self.wait_element(element)
        self.find_element(element).clear()
        self.find_element(element).send_keys(text)

    def click(self, element):
        """
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
        driver.click("id=kw")
        """
        self.wait_element(element)
        self.find_element(element).click()

    def right_click(self, element):
        """
        Right click element.

        Usage:
        driver.right_click("class=right")
        """
        self.wait_element(element)
        ActionChains(self.driver).context_click(self.find_element(element)).perform()

    def move_to_element(self, element):
        '''
        Mouse over the element.

        Usage:
        driver.move_to_element("css=choose")
        '''
        self.wait_element(element)
        ActionChains(self.driver).move_to_element(self.find_element(element)).perform()

    def double_click(self, element):
        """
        Double click element.

        Usage:
        driver.double_click("name=baidu")
        """
        self.wait_element(element)
        ActionChains(self.driver).double_click(self.find_element(element)).perform()

    def drag_and_drop(self, source_element, target_element):
        """
        Drags an element a certain distance and then drops it.

        Usage:
        driver.drag_and_drop("id=s","id=t")
        """
        self.wait_element(source_element)
        self.wait_element(target_element)
        ActionChains(self.driver).drag_and_drop(self.find_element(source_element),
                                                self.find_element(target_element)).perform()

    def back(self):
        """
        Back to old window.

        Usage:
        driver.back()
        """
        self.driver.back()

    def forward(self):
        """
        Forward to old window.

        Usage:
        driver.forward()
        """
        self.driver.forward()

    def get_attribute(self, element, attribute):
        """
        Gets the value of an element attribute.

        Usage:
        driver.get_attribute("id=kw","attribute")
        """
        self.wait_element(element)
        return self.find_element(element).get_attribute(attribute)

    def get_text(self, element):
        """
        Get element text information.

        Usage:
        driver.get_text("name=johnny")
        """
        self.wait_element(element)
        return self.find_element(element).text

    def get_display(self, element):
        """
        Gets the element to display,The return result is true or false.

        Usage:
        driver.get_display("id=ppp")
        """
        self.wait_element(element)
        return self.find_element(element).is_displayed()

    def get_title(self):
        """
        Get window title.

        Usage:
        driver.get_title()
        """
        return self.driver.title

    def get_url(self):
        """
        Get the URL address of the current page.

        Usage:
        driver.get_url()
        """
        return self.driver.current_url

    def get_screenshot(self, file_path):
        """
        Get the current window screen_shoot.

        Usage:
        driver.get_screenshot("./pic.png")
        """
        self.driver.get_screenshot_as_file(file_path)

    def submit(self, element):
        """
        Submit the specified form.

        Usage:
        driver.submit("id=mainFrame")
        """
        self.wait_element(element)
        self.find_element(element).submit()

    def switch_to_frame(self, element):
        """
        Switch to the specified frame.

        Usage:
        driver.switch_to_frame("id=mainFrame")
        """
        self.wait_element(element)
        self.driver._switch_to_frame(self.find_element(element))

    def switch_to_frame_out(self):
        """
        Returns the current form machine form at the next higher level.
        Corresponding relationship with switch_to_frame () method.

        Usage:
        driver.switch_to_frame_out()
        """
        self.driver.switch_to.default_content()

    def open_new_window(self, element):
        """
        Open the new window and switch the handle to the newly opened window.

        Usage:
        driver.open_new_window(id=johnny)
        """
        current_windows = self.driver.current_window_handle
        self.find_element(element).click()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != current_windows:
                self.driver.switch_to.window(handle)

    def F5(self):
        '''
        Refresh the current page.

        Usage:
        driver.F5()
        '''
        self.driver.refresh()

    def js(self, script):
        """
        Execute JavaScript scripts.

        Usage:
        driver.js("window.scrollTo(200,1000);")
        """
        self.driver.execute_script(script)

    def swipe(self, js="window.scrollTo(100,450)"):
        """
        selenium实现页面滑动需要借助网页的js,用driver中的execute_script方法执行js
        window.scrollTo(X,Y)方法可以实现滑动效果.
        x代表窗口文档显示区左上角显示的文档的 x 坐标
        y代表窗口文档显示区左上角显示的文档的 y 坐标

        """
        self.driver.execute_script(js)

    def accept_alert(self):
        """
        Accept warning box.

        Usage:
        driver.accept_alert()
        """
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        """
        Dismisses the alert available.

        Usage:
        driver.dismiss_alert()
        """
        self.driver.switch_to.alert.dismiss()

    def close(self):
        """
        Close the windows.

        Usage:
        driver.close()
        """
        self.driver.close()

    def quit(self):
        """
        Quit the driver and close all the windows.

        Usage:
        driver.quit()
        """
        self.driver.quit()
