from sentseg.tests import *

class TestSegController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='seg', action='index'))
        # Test response...
