from WasRun import WasRun
from TestCase import *

class TestCaseTest(TestCase):

    def testTemplateMethod(self):
        self.test = WasRun("testMethod")
        self.test.run()
        assert("setUp testMethod tearDown " == self.test.log)

    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert("1 run, 0 failed" == result.summary())

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        result = test.run()
        assert("1 run, 1 failed" == result.summary())


TCT = TestCaseTest("testTemplateMethod")
TCT.run()
TCT.testResult()
TCT.testFailedResult()

# print TCT.test.__class__
# print TCT.test.name
#
# print TCT.__class__
# print TCT.name

# print issubclass(TestCaseTest, TestCase)
# print issubclass(WasRun, TestCase)

print "Compiled and ran"
