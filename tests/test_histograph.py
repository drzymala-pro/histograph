# -*- coding: utf-8 -*-

import histograph
import unittest


# To debug any specific case, add this the line above:
# import pdb; pdb.set_trace()



class HistographTestCase(unittest.TestCase):

    def setUp(self):
        self.histograph = histograph.Histograph()
        self.hist = self.histograph.get_histogram



class MakeMarkerTest(HistographTestCase):

    def test_returns_integer(self):
        marker = self.histograph.make_marker(2000,1,2,3,4,5)
        self.assertEqual(int, type(marker))

    def test_returns_valid_unix_timestamp(self):
        unix_time = self.histograph.make_marker
        self.assertEqual(unix_time(1970,1,1,0,0,1), 1)
        self.assertEqual(unix_time(2020,5,4,3,2,1), 1588561321)



class InvalidParametersTest(HistographTestCase):

    def test_raises_error_on_invalid_resolution(self):
        self.assertRaises(Exception, self.hist, resolution=5.5)
        self.assertRaises(Exception, self.hist, resolution=0)
        self.assertRaises(Exception, self.hist, resolution=-1)
        self.assertRaises(Exception, self.hist, resolution=-77)



class EmptyHistograph(HistographTestCase):

    def test_histogram_is_all_zeros(self):
        self.assertEqual(self.hist(1), [0])
        self.assertEqual(self.hist(2), [0,0])
        self.assertEqual(self.hist(3), [0,0,0])
        self.assertEqual(self.hist(4), [0,0,0,0])
        self.assertEqual(self.hist(5), [0,0,0,0,0])
        self.assertEqual(self.hist(5, first=50), [0,0,0,0,0])
        self.assertEqual(self.hist(5, last=100), [0,0,0,0,0])
        self.assertEqual(self.hist(5, first=50, last=100), [0,0,0,0,0])
        self.assertEqual(self.hist(5, first=100, last=50), [0,0,0,0,0])
        self.assertEqual(self.hist(5, first=-50, last=-100), [0,0,0,0,0])
        self.assertEqual(self.hist(5, first=-100, last=-50), [0,0,0,0,0])



class SingleValueHistograph(HistographTestCase):

    def setUp(self):
        super(SingleValueHistograph, self).setUp()
        self.histograph.add_marker(0)

    def test_histogram_is_correct(self):
        self.assertEqual(self.hist(1), [1])
        self.assertEqual(self.hist(2), [1,0])
        self.assertEqual(self.hist(3), [1,0,0])
        self.assertEqual(self.hist(4), [1,0,0,0])
        self.assertEqual(self.hist(5), [1,0,0,0,0])

    def test_obeys_first_bounding_parameter(self):
        self.assertEqual(self.hist(resolution=1, first=-1), [1])
        self.assertEqual(self.hist(resolution=2, first=-1), [0,1])
        self.assertEqual(self.hist(resolution=3, first=-1), [0,0,1])
        self.assertEqual(self.hist(resolution=4, first=-1), [0,0,0,1])
        self.assertEqual(self.hist(resolution=5, first=-1), [0,0,0,0,1])

    def test_obeys_last_bounding_parameter(self):
        self.assertEqual(self.hist(resolution=1, last=1), [1])
        self.assertEqual(self.hist(resolution=2, last=1), [1,0])
        self.assertEqual(self.hist(resolution=3, last=1), [1,0,0])
        self.assertEqual(self.hist(resolution=4, last=1), [1,0,0,0])
        self.assertEqual(self.hist(resolution=5, last=1), [1,0,0,0,0])

    def test_obeys_both_bounding_parameters(self):
        self.assertEqual(self.hist(resolution=1,  first=-1, last=1), [1])
        self.assertEqual(self.hist(resolution=2,  first=-1, last=1), [1,0])
        self.assertEqual(self.hist(resolution=3,  first=-1, last=1), [0,1,0])
        self.assertEqual(self.hist(resolution=4,  first=-1, last=1), [0,1,0,0])
        self.assertEqual(self.hist(resolution=5,  first=-1, last=1), [0,0,1,0,0])
        self.assertEqual(self.hist(resolution=9,  first=-1, last=1), [0,0,0,0,1,0,0,0,0])
        self.assertEqual(self.hist(resolution=10, first=-1, last=1), [0,0,0,0,1,0,0,0,0,0])



class FlatHistogramCheck(HistographTestCase):

    def setUp(self):
        super(FlatHistogramCheck, self).setUp()
        # Add 10 points evenly distributed
        self.histograph.add_marker(0)
        self.histograph.add_marker(1)
        self.histograph.add_marker(2)
        self.histograph.add_marker(3)
        self.histograph.add_marker(4)
        self.histograph.add_marker(5)
        self.histograph.add_marker(6)
        self.histograph.add_marker(7)
        self.histograph.add_marker(8)
        self.histograph.add_marker(9)

    def test_histogram_is_correct(self):
        self.assertEqual(self.hist(1),  [10])
        self.assertEqual(self.hist(2),  [5,5])
        self.assertEqual(self.hist(3),  [4,3,3])
        self.assertEqual(self.hist(4),  [3,2,2,3])
        self.assertEqual(self.hist(5),  [2,2,2,2,2])
        self.assertEqual(self.hist(6),  [2,2,1,2,1,2])
        self.assertEqual(self.hist(7),  [2,1,1,2,1,1,2])
        self.assertEqual(self.hist(8),  [2,1,1,1,1,1,1,2])
        self.assertEqual(self.hist(9),  [2,1,1,1,1,1,1,1,1])
        self.assertEqual(self.hist(10), [1,1,1,1,1,1,1,1,1,1])
        self.assertEqual(self.hist(11), [1,1,1,1,1,0,1,1,1,1,1])
        self.assertEqual(self.hist(12), [1,1,1,1,0,1,1,1,0,1,1,1])
        self.assertEqual(self.hist(13), [1,1,1,0,1,1,0,1,1,0,1,1,1])
        self.assertEqual(self.hist(14), [1,1,0,1,1,0,1,1,0,1,1,0,1,1])
        self.assertEqual(self.hist(15), [1,1,0,1,1,0,1,0,1,1,0,1,0,1,1])
        self.assertEqual(self.hist(16), [1,1,0,1,0,1,0,1,1,0,1,0,1,0,1,1])
        self.assertEqual(self.hist(17), [1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1])
        self.assertEqual(self.hist(18), [1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1])
        self.assertEqual(self.hist(19), [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1])
        self.assertEqual(self.hist(20), [1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1])
        self.assertEqual(self.hist(21), [1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,0,1,0,1,0,1])
        self.assertEqual(self.hist(22), [1,0,1,0,1,0,0,1,0,1,0,0,1,0,1,0,0,1,0,1,0,1])
        self.assertEqual(self.hist(23), [1,0,1,0,0,1,0,1,0,0,1,0,1,0,0,1,0,1,0,0,1,0,1])
        self.assertEqual(self.hist(24), [1,0,1,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0,1,0,0,1,0,1])
        self.assertEqual(self.hist(25), [1,0,1,0,0,1,0,0,1,0,0,1,0,1,0,0,1,0,0,1,0,0,1,0,1])
        self.assertEqual(self.hist(26), [1,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,1])
        self.assertEqual(self.hist(27), [1,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1])
        self.assertEqual(self.hist(28), [1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1])
        self.assertEqual(self.hist(29), [1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1])
        self.assertEqual(self.hist(30), [1,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,1])

    def test_obeys_first_bounding_parameter(self):
        self.assertEqual(self.hist(resolution=1, first=5), [5])
        self.assertEqual(self.hist(resolution=2, first=5), [3,2])
        self.assertEqual(self.hist(resolution=3, first=5), [2,1,2])
        self.assertEqual(self.hist(resolution=4, first=5), [2,1,1,1])
        self.assertEqual(self.hist(resolution=5, first=5), [1,1,1,1,1])

    def test_obeys_last_bounding_parameter(self):
        self.assertEqual(self.hist(resolution=1, last=4), [5])
        self.assertEqual(self.hist(resolution=2, last=4), [3,2])
        self.assertEqual(self.hist(resolution=3, last=4), [2,1,2])
        self.assertEqual(self.hist(resolution=4, last=4), [2,1,1,1])
        self.assertEqual(self.hist(resolution=5, last=4), [1,1,1,1,1])

    def test_obeys_both_bounding_parameters(self):
        self.assertEqual(self.hist(resolution=1,  first=3, last=6), [4])
        self.assertEqual(self.hist(resolution=2,  first=3, last=6), [2,2])
        self.assertEqual(self.hist(resolution=3,  first=3, last=6), [2,1,1])
        self.assertEqual(self.hist(resolution=4,  first=3, last=6), [1,1,1,1])
        self.assertEqual(self.hist(resolution=5,  first=3, last=6), [1,1,0,1,1])



class GiantPeakHistogramCheck(HistographTestCase):

    def setUp(self):
        super(GiantPeakHistogramCheck, self).setUp()
        # Add one giant peak
        self.histograph.add_marker(5)
        self.histograph.add_marker(5)
        self.histograph.add_marker(5)
        self.histograph.add_marker(5)
        self.histograph.add_marker(5)
        self.histograph.add_marker(5)
        self.histograph.add_marker(5)
        self.histograph.add_marker(5)
        self.histograph.add_marker(5)
        self.histograph.add_marker(5)

    def test_still_flat_if_no_bounds_given(self):
        self.assertEqual(self.hist(resolution=1), [10])
        self.assertEqual(self.hist(resolution=2), [5,5])
        self.assertEqual(self.hist(resolution=3), [4,3,3])
        self.assertEqual(self.hist(resolution=4), [3,3,2,2])
        self.assertEqual(self.hist(resolution=5), [2,2,2,2,2])

    def test_keep_the_peak_if_bounds_given(self):
        self.assertEqual(self.hist(resolution=1,  first=0, last=10), [10])
        self.assertEqual(self.hist(resolution=2,  first=0, last=10), [10,0])
        self.assertEqual(self.hist(resolution=3,  first=0, last=10), [0,10,0])
        self.assertEqual(self.hist(resolution=4,  first=0, last=10), [0,10,0,0])
        self.assertEqual(self.hist(resolution=5,  first=0, last=10), [0,0,10,0,0])


