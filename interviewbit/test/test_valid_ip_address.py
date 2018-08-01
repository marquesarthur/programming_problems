import unittest
from interviewbit.stringm.valid_ip_address import Solution


class RestoreIpAddressTest(unittest.TestCase):
    
    def test_base_case(self):
        s = Solution()
        A = "12340"
        B = ["1.2.3.40", "1.2.34.0", "1.23.4.0", "12.3.4.0"]

        result = s.restoreIpAddresses(A)
        self.assertEqual(result, B)

    def test_other_case(self):
        s = Solution()
        A = "0100100"
        B = ["0.10.0.100", "0.100.10.0"]
        result = s.restoreIpAddresses(A)
        self.assertEqual(result, B)
