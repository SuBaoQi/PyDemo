import unittest
from HTMLTestRunner import HTMLTestRunner
from BeautifulReport import BeautifulReport

loader = unittest.TestLoader()
discover = loader.discover(r'/Users/subaoqi/coder/Projects/PyDemo/unittest_demo/lemon_test')

# runner = HTMLTestRunner(stream=open("report.html", "wb"))
# runner.run(discover)

report = BeautifulReport(discover)
report.report("椰子树报告", "bp_report.html")
