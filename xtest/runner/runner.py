import os
import time
import inspect
import webbrowser
import unittest
from xtest.config import XTest
from selenium import webdriver
from xtest.runner.HTMLTestRunner import HTMLTestRunner

browsers = ["chrome", "firefox", "gc", "ff"]


def main(path=None, browser=None, debug=False, timeout=10, title=None, description=None):
    """
    入口方法
    :param path: 运行的文件
    :param browser: 浏览器
    :param debug: 浏览器
    :param timeout: 超时时间
    :param title: 报告的名称
    :param description: 报告的描述
    :return:
    """
    stack_t = inspect.stack()
    ins = inspect.getframeinfo(stack_t[1][0])
    run_path = os.path.dirname(os.path.abspath(ins.filename))

    # 全局启动浏览器
    if browser is None:
        browser = "chrome"
    if browser not in browsers:
        raise NameError(f"不支持{browser}浏览器.")
    if browser in ["chrome", "gc"]:
        XTest.driver = webdriver.Chrome()
    if browser in ["firefox", "ff"]:
        XTest.driver = webdriver.Firefox()

    # 全局超时时间
    XTest.timeout = timeout

    if path is None:
        path = os.getcwd()
    suit = unittest.defaultTestLoader.discover(start_dir=path)

    if debug is False:
        reports_dir = os.path.join(run_path, "reports")
        if os.path.exists(reports_dir) is False:
            os.mkdir(reports_dir)

        # HTML格式的报告 ，XML 格式的报告
        now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
        report_file = os.path.join(reports_dir,  f"{now_time}_result.html")
        with(open(report_file, 'wb')) as fp:
            runner = HTMLTestRunner(stream=fp, title=title, description=description)
            runner.run(suit)
            print(f"生成测试报告：{report_file}")
            webbrowser.open_new("file:///{}".format(report_file))
    else:
        runner = unittest.TextTestRunner()
        runner.run(suit)

    # 全局的关闭浏览器
    if XTest.driver is not None:
        XTest.driver.quit()













