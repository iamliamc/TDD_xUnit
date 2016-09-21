from WasRun import WasRun
from TestCase import TestCase

class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")

    def testRunning(self):
        self.test.run()
        assert(self.test.wasRun)

    def testSetUp(self):
        self.test.run()
        assert(self.test.wasSetup)

TCT = TestCaseTest("testRunning")
TCT.run()

print TCT.test.__class__
print TCT.test.name

print TCT.__class__
print TCT.name

# print issubclass(TestCaseTest, TestCase)
# print issubclass(WasRun, TestCase)

print "Compiled and ran"
