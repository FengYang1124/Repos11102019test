import unittest
from time import sleep
from selenium import webdriver

class TestBaidu(unittest.TestCase):
    '''百度搜索'''

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.base_url = "https://baidu.com"
        print("setUpClass")

    # def setUp(self):
    #     self.driver=webdriver.Chrome()
    #     self.base_url=  "https://baidu.com"
    #     print("setUp")

    def baidu_search(self,search_key):
        """将操作步骤封装成一个方法baidu_search"""
        self.driver.get(self.base_url)#获取地址
        self.driver.find_element_by_id("kw").send_keys(search_key)#定位输入框并输入selenium
        self.driver.find_element_by_id("su").click()#定位“百度一下”按钮并点击
        sleep(2)#休眠2秒
        self.title=self.driver.title


    def test2_search_key_selenium(self):
        """case1"""
        search_key="selenium"
        self.baidu_search(search_key)
        self.assertEqual(self.title,search_key+"_百度搜索")

    def test1_search_key_unittest(self):
        """case2"""
        search_key="unittest"
        self.baidu_search(search_key)
        self.assertEqual(self.title,search_key+"_百度搜索")


    # def tearDown(self):
    #     self.driver.quit()
    #     print("tearDown")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("tearDownClass")

    if __name__=="__main__":
        unittest.main()

