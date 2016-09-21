class TestCase:
    def __init__(self, name):
        self.name = name

    # def setUp(self):
    #     print "TestCase.setUp --> Pass"
    #     pass

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()
