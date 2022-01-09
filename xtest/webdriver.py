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


class WebDriver:

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

    def __find_element(self, index, **kwargs):
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
            if index is None:
                self.__wait_element(By.ID, value)
            elem = XTest.driver.find_elements(By.ID, value)
        elif by == "name":
            if index is None:
                self.__wait_element(By.NAME, value)
            elem = XTest.driver.find_elements(By.NAME, value)
        elif by == "class_name":
            if index is None:
                self.__wait_element(By.CLASS_NAME, value)
            elem = XTest.driver.find_elements(By.CLASS_NAME, value)
        elif by == "tag":
            if index is None:
                self.__wait_element(By.TAG_NAME, value)
            elem = XTest.driver.find_elements(By.TAG_NAME, value)
        elif by == "xpath":
            if index is None:
                self.__wait_element(By.XPATH, value)
            elem = XTest.driver.find_elements(By.XPATH, value)
        elif by == "link_text":
            if index is None:
                self.__wait_element(By.LINK_TEXT, value)
            elem = XTest.driver.find_elements(By.LINK_TEXT, value)
        elif by == "partial_link_text":
            if index is None:
                self.__wait_element(By.PARTIAL_LINK_TEXT, value)
            elem = XTest.driver.find_elements(By.PARTIAL_LINK_TEXT, value)
        elif by == "css":
            if index is None:
                self.__wait_element(By.CSS_SELECTOR, value)
            elem = XTest.driver.find_elements(By.CSS_SELECTOR, value)
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

    def type(self, text, clear=False, enter=False, index=None, **kwargs):
        """
        输入
        :param text: 文本
        :param clear: 是否清除输入框
        :param enter: 是否回车
        :param kwargs:
        :return:
        """
        elem = self.__find_element(index, **kwargs)
        if clear is True:
            elem.clear()

        if index is None:
            index = 0
        elem[index].send_keys(text)
        if enter is True:
            elem.send_keys("\n")

    def click(self, index=None, **kwargs):
        """
        点击
        :param kwargs:
        :return:
        """
        elem = self.__find_element(index, **kwargs)
        if index is None:
            index = 0
        elem[index].click()

    def get_text(self, index=None, **kwargs):
        """
        获取元素的文本
        :param kwargs:
        :return:
        """
        elem = self.__find_element(index, **kwargs)
        if index is None:
            index = 0
        return elem[index].text

    @property
    def get_title(self):
        """
        获取元素的标题
        :return:
        """
        title = XTest.driver.title
        return title

    def get_elements(self, **kwargs):
        elem = self.__find_element(None, **kwargs)
        return elem





