#import People class
from people.people import People

#In order to test People class, the test case class must start with "test"
class TestPeople:

    def test_weight(self):
        p1 = People('Mark', 22, 130, 'CityU')
        assert p1.get_weight() ==130

        p1.lose_weight(5)
        assert p1.get_weight() == 125