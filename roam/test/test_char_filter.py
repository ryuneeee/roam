import unittest
from detector.detector import CharFilter

class TestCharFilter(unittest.TestCase):

    def setUp(self):
        super().setUp()

    def test_next(self):
        cf = CharFilter('RO-AM', 'R-OAM2', 'ROA-M3').remove_dash().lower()
        self.assertEquals('roam', cf.get(0))
        self.assertEquals('roam2', cf.next())
        self.assertEquals('roam3', cf.next())
        self.assertRaises(IndexError, cf.next)

    def test_get(self):
        cf = CharFilter('ROA-M', 'RO-AM2', 'R-OA-M3', 'RO-A-M4').remove_dash().lower()
        self.assertEquals('roam', cf.get(0))
        self.assertEquals('roam2', cf.get(1))
        self.assertEquals('roam3', cf.get(2))
        self.assertEquals('roam4', cf.next())
        self.assertRaises(IndexError, cf.get, 4)

    def test_lower(self):
        cf = CharFilter('ROA-M', 'RO-AM2').remove_dash().lower()
        assert 'roam' == cf.get(0)
        assert 'roam2' == cf.next()

    def test_tuple(self):
        tup = ('R-O-AM', 'RO--AM2', 'RO-AM3', '-ROAM4')
        result_tup = ('roam', 'roam2', 'roam3', 'roam4')
        cf = CharFilter(*tup).remove_dash().lower()
        self.assertEqual(result_tup, cf.get_tuple())

    def test_remove_dot(self):
        cf = CharFilter('.d..o.t..').remove_dot()
        self.assertEqual('dot', cf.first())

    def test_remove_whitespace(self):
        cf = CharFilter(' s  p   a c e  ').remove_whitespace()
        self.assertEqual('space', cf.first())

    def test_remove_dash(self):
        cf = CharFilter('-d-a--sh-').remove_dash()
        self.assertEqual('dash', cf.first())

    def test_remove_underbar(self):
        cf = CharFilter('_und__er_b_a_r__').remove_underbar()
        self.assertEqual('underbar', cf.first())

    def test_remove_basic(self):
        cf = CharFilter(' _b-a_- .s.i_ c--', '-b-_- a* s--i c--').remove_basic()
        self.assertEqual('basic', cf.first())
        self.assertEqual('ba*sic', cf.next())

    def test_remove_special(self):
        cf = CharFilter('!s#%p@$e#$%c;:{<\\>}&[]!?=+~i;a\'l',
                    '!s#%p@$e #$-%c_;:{<>}&[]!?=+~i;a\'l -.').remove_special()
        self.assertEqual('special', cf.first())
        self.assertEqual('spe -c_ial -.', cf.next())

    def test_remove_advanced(self):
        cf = CharFilter('$^#a#$%!#d`@%</.,{}[]>v;/a@nc~!%&$#^& -_=+-(:;"\'\\ed',
                    '1a2#$d3v;! ,:;~4a5n6c7e8d9').remove_advanced()
        self.assertEqual('advanced', cf.first())
        self.assertEqual('1a2d3v4a5n6c7e8d9', cf.next())


    def tearDown(self):
        super().tearDown()