import xtest


class BaiduTest(xtest.TestCase):

    def test_baidu(self):
        self.open("http://www.baidu.com")
        self.type(id_="kw", text="xtest")
        self.click(css="#su")
        self.sleep(2)

    def test_baidu2(self):
        self.open("http://www.baidu.com")
        # self.type(xpath="//*[@id='kw']", text="unittest")
        # self.click(css="#su")
        # self.sleep(2)
        text = self.get_text(class_name="s-bottom-layer-content")
        print(text)


if __name__ == '__main__':
    xtest.main(browser="firefox", timeout=2)



