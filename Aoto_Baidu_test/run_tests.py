import unittest
from test_report.HTMLTestRunner import HTMLTestRunner
import time

#定义测试用例的目录为当前目录下的test_case目录
test_dir="./test_case"
suits=unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")

#获取当前日期时间
nowTime=time.strftime("%Y-%m-%d %H_%M_%S")
if __name__=="__main__":

    #生成HTHL格式的报告
    file=open("./test_report/"+nowTime+"result.html","wb")
    runner = HTMLTestRunner(stream=file,
                          title="BaiduSearchTestReport_百度搜索测试报告",
                          description="运行环境:Windows10,Chrome浏览器")
    runner.run(suits)
    file.close()