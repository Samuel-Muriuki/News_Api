import unittest
from app.models import Sources

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources('The New York Times','Sports',"In an attempt to revive flagging interest in women's badminton as the 2012 London Olympics approach, officials governing the sport have decided that its female athletes need to appear more, how to put it, womanly.", " To create a more “attractive presentation,” the Badminton World Federation has decreed that women must wear skirts or dresses to play at the elite level, beginning Wednesday. ",'2016-03-01T15:43:26Z','https://www.nytimes.com/2011/05/27/sports/badminton-dress-code-for-women-criticized-as-sexist.html','https://static01.nyt.com/images/2011/05/27/sports/BADMINTON/BADMINTON-jumbo.jpg?quality=75&auto=webp',"Badminton's New Dress Code Is Being Criticized as Sexist")

    def test_instance(self):
        '''
        Test to check creation of new article Source instance
        '''
        self.assertTrue(isinstance(self.new_source,Sources))

