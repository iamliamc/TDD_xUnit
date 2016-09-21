from WasRun import WasRun
from TestCase import *

class TestCaseTest(TestCase):

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        result = TestResult()
        test.run(result)
        assert("setUp testMethod tearDown " == test.log)

    def testResult(self):
        test = WasRun("testMethod")
        result = TestResult()
        test.run(result)
        assert("1 run, 0 failed" == result.summary())

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        result = TestResult()
        test.run(result)
        assert("1 run, 1 failed" == result.summary())

    def testFailedResultFormatting(self):
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert("1 run, 1 failed" == result.summary())

    def testSuite(self):
        suite = TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        result = TestResult()
        suite.run(result)
        assert("2 run, 1 failed" == result.summary)

suite = TestSuite()
for test in ["testTemplateMethod", "testResult", "testFailedResultFormatting", "testFailedResultFormatting", "testFailedResult", "testSuite"]:
    suite.add(TestCaseTest(test))
result = TestResult()
suite.run(result)
print result.summary()


# TCT = TestCaseTest("testTemplateMethod")
# TCT.run()
# TCT.testResult()
# TCT.testFailedResult()

# print TCT.test.__class__
# print TCT.test.name
#
# print TCT.__class__
# print TCT.name

# print issubclass(TestCaseTest, TestCase)
# print issubclass(WasRun, TestCase)

print "Compiled and ran"
