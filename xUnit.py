from WasRun import WasRun
from TestCase import TestCase

class TestCaseTest(TestCase):

    def testTemplateMethod(self):
        self.test = WasRun("testMethod")
        self.test.run()
        assert("setUp testMethod tearDown " == self.test.log)

TCT = TestCaseTest("testTemplateMethod")
TCT.run()

print TCT.test.__class__
print TCT.test.name

print TCT.__class__
print TCT.name

# print issubclass(TestCaseTest, TestCase)
# print issubclass(WasRun, TestCase)

print "Compiled and ran"
