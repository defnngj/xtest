import os
import unittest
from .config import XTest
from selenium import webdriver


browsers = ["chrome", "firefox"]


def main(path=None, browser=None, timeout=10):
    """
    入口方法
    :param path: 运行的文件
    :param browser: 浏览器
    :param timeout: 超时时间
    :return:
    """
    if browser is None:
        browser = "chrome"
    if browser not in browsers:
        raise NameError(f"不支持{browser}浏览器.")
    if browser == "chrome":
        XTest.driver = webdriver.Chrome()
    if browser == "firefox":
        XTest.driver = webdriver.Firefox()

    # 全局超时时间
    XTest.timeout = timeout

    if path is None:
        path = os.getcwd()
    suit = unittest.defaultTestLoader.discover(start_dir=path)
    runner = unittest.TextTestRunner()
    runner.run(suit)

    # 全局的关闭浏览器
    if XTest.driver is not None:
        XTest.driver.quit()













