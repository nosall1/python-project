#-*- coding:utf-8 -*-
import unittest


def baseTest(testClass):
    # 装载测试用例
    test_cases = unittest.TestLoader().loadTestsFromTestCase(testClass)
        # 使用测试套件并打包测试用例
    test_suit = unittest.TestSuite()
    test_suit.addTests(test_cases)
    # 运行测试套件，并返回测试结果
    test_result = unittest.TextTestRunner(verbosity=2).run(test_suit)
    #生成测试报告
    print("testsRun:%s" % test_result.testsRun)
    print("failures:%s" % len(test_result.failures))
    print("errors:%s" % len(test_result.errors))
    print("skipped:%s" % len(test_result.skipped))