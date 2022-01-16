import os
import argparse
from xtest import __version__, __description__
from webdriver_manager.firefox import GeckoDriverManager
from xtest.utils.webdriver_manager_extend import ChromeDriverManager


def main():
    """
    命令行工具
    """

    parser = argparse.ArgumentParser(description=__description__)

    parser.add_argument(
        '-v', '--version', dest='version', action='store_true',
        help="show version")

    parser.add_argument(
        '-project',
        help="Create an xtest automation test project.")

    parser.add_argument(
        '-install',
        help="Install the browser driver, For example, 'chrome', 'firefox'. ")

    args = parser.parse_args()

    if args.version:
        print("xtest {}".format(__version__))
        return 0

    project_name = args.project
    if project_name:
        create_scaffold(project_name)
        return 0

    driver_name = args.install
    if driver_name:
        install_driver(driver_name)
        return 0


def create_scaffold(project_name):
    """
    create scaffold with specified project name.
    """
    if os.path.isdir(project_name):
        print(u"Folder {} exists, please specify a new folder name.".format(project_name))
        return

    print("Start to create new test project: {}".format(project_name))
    print("CWD: {}\n".format(os.getcwd()))

    def create_folder(path):
        os.makedirs(path)
        msg = "created folder: {}".format(path)
        print(msg)

    def create_file(path, file_content=""):
        with open(path, 'w') as f:
            f.write(file_content)
        msg = "created file: {}".format(path)
        print(msg)


    test_sample = '''import xtest


class SampleTest(xtest.TestCase):

    def test_case(self):
        """a simple test case """
        self.open("https://www.baidu.com")
        self.assertInTitle("百度一下")


if __name__ == '__main__':
    xtest.main(browser="firefox", debug=True)
'''

    run_test = """import xtest
if __name__ == '__main__':
    xtest.main(path="./test_dir/", browser="firefox",)
"""

    create_folder(project_name)
    create_folder(os.path.join(project_name, "test_dir"))
    create_folder(os.path.join(project_name, "reports"))
    create_file(os.path.join(project_name, "test_dir", "test_sample.py"), test_sample)
    create_file(os.path.join(project_name, "run.py"), run_test)


def install_driver(browser=None):
    """
    Download and install the browser driver
    :param browser: The Driver to download. Pass as `chrome/firefox/ie/edge/opera`. Default Chrome.
    :return:
    """

    if browser is None:
        browser = "chrome"

    if browser == "chrome":
        ChromeDriverManager().install()
    elif browser == "firefox":
        GeckoDriverManager().install()
    else:
        raise NameError(f"Not found '{browser}' browser driver.")









