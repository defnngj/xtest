import unittest
import time
from .config import XTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


LOCATOR_LIST = {
    'css': By.CSS_SELECTOR,
    'id_': By.ID,
    'name': By.NAME,
    'xpath': By.XPATH,
    'link_text': By.LINK_TEXT,
    'partial_link_text': By.PARTIAL_LINK_TEXT,
    'tag': By.TAG_NAME,
    'class_name': By.CLASS_NAME,
}


class TestCase(unittest.TestCase):

    def __wait_element(self, by, value):
        """
        元素显示等待
        :param by:
        :param value:
        :return:
        """
        try:
            WebDriverWait(XTest.driver, XTest.timeout, 0.5).until(
                EC.visibility_of_element_located((by, value))
            )
        except TimeoutException:
            raise TimeoutException("查找元素超时")

    def __find_element(self, **kwargs):
        if not kwargs:
            raise ValueError("Please specify a locator")
        if len(kwargs) > 1:
            raise ValueError("Please specify only one locator")

        by, value = next(iter(kwargs.items()))
        try:
            LOCATOR_LIST[by]
        except KeyError:
            raise ValueError("Element positioning of type '{}' is not supported. ".format(by))

        if by == "id_":
            self.__wait_element(By.ID, value)
            elem = XTest.driver.find_element(By.ID, value)
        elif by == "name":
            self.__wait_element(By.NAME, value)
            elem = XTest.driver.find_element(By.NAME, value)
        elif by == "class_name":
            self.__wait_element(By.CLASS_NAME, value)
            elem = XTest.driver.find_element(By.CLASS_NAME, value)
        elif by == "tag":
            self.__wait_element(By.TAG_NAME, value)
            elem = XTest.driver.find_element(By.TAG_NAME, value)
        elif by == "xpath":
            self.__wait_element(By.XPATH, value)
            elem = XTest.driver.find_element(By.XPATH, value)
        elif by == "link_text":
            self.__wait_element(By.LINK_TEXT, value)
            elem = XTest.driver.find_element(By.LINK_TEXT, value)
        elif by == "partial_link_text":
            self.__wait_element(By.PARTIAL_LINK_TEXT, value)
            elem = XTest.driver.find_element(By.PARTIAL_LINK_TEXT, value)
        elif by == "css":
            self.__wait_element(By.CSS_SELECTOR, value)
            elem = XTest.driver.find_element(By.CSS_SELECTOR, value)
        else:
            raise ValueError(f"{by}类型不支持. ")
        return elem

    def open(self, url):
        """打开浏览器"""
        self.driver = XTest.driver
        XTest.driver.get(url)

    def close(self):
        """
        关闭浏览器，如果有多个窗口，只关闭一个。
        :return:
        """
        XTest.driver.close()

    def close_all(self):
        """
        关闭浏览器，如果有多个窗口，全部关闭
        :return:
        """
        XTest.driver.quit()

    def sleep(self, sec):
        """
        休眠
        :param sec: 单位秒
        :return:
        """
        time.sleep(sec)

    class Id():

        def __init__(self, id):
            self.elem = XTest.driver.find_element(By.ID, id)

        def set_text(self, text):
            self.elem.send_keys(text)

        def click(self):
            self.elem.click()

    class CSS():

        def __init__(self, css):
            self.elem = XTest.driver.find_element(By.CSS_SELECTOR, css)

        def set_text(self, text):
            self.elem.send_keys(text)

        def click(self):
            self.elem.click()

    def type(self, text, clear=False, enter=False, **kwargs):
        """
        输入
        :param text: 文本
        :param clear: 是否清除输入框
        :param enter: 是否回车
        :param kwargs:
        :return:
        """
        elem = self.__find_element(**kwargs)
        if clear is True:
            elem.clear()
        elem.send_keys(text)
        if enter is True:
            elem.send_keys("\n")

    def click(self, **kwargs):
        """
        点击
        :param kwargs:
        :return:
        """
        elem = self.__find_element(**kwargs)
        elem.click()

    def get_text(self, **kwargs):
        """
        获取元素的文本
        :param kwargs:
        :return:
        """
        elem = self.__find_element(**kwargs)
        return elem.text















