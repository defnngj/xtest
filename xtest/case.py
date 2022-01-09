import unittest
from .config import XTest
from xtest.webdriver import WebDriver


class TestCase(unittest.TestCase, WebDriver):

    def assertTitle(self, title=None):
        """
        断言当前标题是否是title
        :param title:
        :return:
        """
        if title is None:
            raise NameError("title不能为空")
        now_title = XTest.driver.title
        self.assertEqual(now_title, title)

    def assertInTitle(self, title):
        """
        断言当前标题是否包含title
        :param title:
        :return:
        """
        if title is None:
            raise NameError("title不能为空")
        now_title = XTest.driver.title
        self.assertIn(title, now_title)

    def assertUrl(self, url=None):
        """
        断言当前地址是否是url
        :param url:
        :return:
        """
        if url is None:
            raise NameError("title不能为空")
        now_url = XTest.driver.current_url
        self.assertEqual(now_url, url)

    def assertInUrl(self, url):
        """
        断言当前地址是否包含url
        :param url:
        :return:
        """
        if url is None:
            raise NameError("title不能为空")
        now_url = XTest.driver.current_url
        self.assertIn(url, now_url)

    def assertText(self, text, index=None, **kwargs):
        """
        断言元素的文本
        """
        if text is None:
            raise NameError("text不能为空")
        element_text = self.get_text(**kwargs, index=index)
        self.assertEqual(element_text, text)














