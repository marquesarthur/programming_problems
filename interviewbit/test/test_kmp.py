import unittest
from interviewbit.stringm.kmp import KMP


class KMPTest(unittest.TestCase):
    
    def test_base_case(self):
        s = KMP()
        pattern = "ABCDABD"
        str = "ABC ABCDAB ABCDABCDABDE"
        ret = [15]

        result = s.search(pattern, str)
        self.assertEqual(result, ret)

    def test_two_matches(self):
        s = KMP()
        pattern = "AA"
        str = "AABC AA AAD ASAA"
        ret = [0, 5, 8, 14]

        result = s.search(pattern, str)
        self.assertEqual(result, ret)