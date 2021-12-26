import xtest
from xtest import date_class, data, file_data


# @date_class(
#     ("name", "keyword"),
#     [("case1", "xtest"),
#      ("case2", "python")
# ])
class BaiduTest(xtest.TestCase):

    def test_baidu(self,):
        print("keyword-->", self.name)
        self.open("http://www.baidu.com")
        self.type(id_="kw", text=self.keyword)
        self.click(css="#su")
        self.sleep(2)

    @data([
        ("case1", "xtest"),
        ("case2", "unittest")
    ])
    def test_baidu2(self):
        self.open("http://www.baidu.com")
        self.type(xpath="//*[@id='kw']", text="unittest")
        self.click(css="#su")
        self.sleep(2)

    @file_data(file="data.csv", line=1)
    def test_baidu2(self):
        self.open("http://www.baidu.com")
        self.type(xpath="//*[@id='kw']", text="unittest")
        self.click(css="#su")
        self.sleep(2)


if __name__ == '__main__':
    xtest.main(browser="firefox",
               timeout=1,
               debug=False,
               title="百度测试报告",
               description="测试环境：windows 11， Firefox")



