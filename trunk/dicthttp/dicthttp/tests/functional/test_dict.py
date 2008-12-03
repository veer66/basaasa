from dicthttp.tests import *

class TestDictController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='dict', action='index'))
        # Test response...
