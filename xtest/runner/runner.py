import os
import time
import inspect
import webbrowser
import unittest
from xtest.config import XTest
from selenium import webdriver
from xtest.runner.HTMLTestRunner import HTMLTestRunner
from xtest.utils.webdriver_manager_extend import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from logzero import logger


browsers = ["chrome", "firefox", "gc", "ff"]

xtest ="""
     ___    ___ _________  _______   ________  _________   
    |\  \  /  /|\___   ___\\  ___ \ |\   ____\|\___   ___\ 
    \ \  \/  / ||___ \  \_\ \   __/|\ \  \___|\|___ \  \_| 
     \ \    / /     \ \  \ \ \  \_|/_\ \_____  \   \ \  \  
      /     \/       \ \  \ \ \  \_|\ \|____|\  \   \ \  \ 
     /  /\   \        \ \__\ \ \_______\____\_\  \   \ \__\
    /__/ /\ __\        \|__|  \|_______|\_________\   \|__|
    |__|/ \|__|                        \|_________|        
                                                 
                                                      
"""

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

    logger.info(xtest)

    # 全局启动浏览器
    if browser is None:
        browser = "chrome"
    if browser not in browsers:
        raise NameError(f"不支持{browser}浏览器.")
    if browser in ["chrome", "gc"]:
        XTest.driver = webdriver.Chrome(ChromeDriverManager().install())
    if browser in ["firefox", "ff"]:
        XTest.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

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
            logger.info(f"生成测试报告：{report_file}")
            webbrowser.open_new("file:///{}".format(report_file))
    else:
        runner = unittest.TextTestRunner()
        runner.run(suit)

    # 全局的关闭浏览器
    if XTest.driver is not None:
        XTest.driver.quit()













