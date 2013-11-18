from . import BaseTestCase

from sealeyes import sealeyes


class TestSealeyes(BaseTestCase):

    def test_something(self):
        self.assertEquals(
            'Hello World!',
            sealeyes(),
        )
