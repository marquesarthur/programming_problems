class Solution:
    def findAllIps(self, A, ips, first_dot, second_dot, third_dot):

        if first_dot <= 3 and second_dot <= 6 and third_dot <= 9 and \
                second_dot - first_dot > 0 and third_dot - second_dot > 0 and len(A) - third_dot > 0:
            ip = (first_dot, second_dot, third_dot)
            a = A[0:ip[0]]
            b = A[ip[0]:ip[1]]
            c = A[ip[1]:ip[2]]
            d = A[ip[2]:len(A)]

            str_ip = self.buildIp(a, b, c, d)
            if self.isValidIp(a, b, c, d) and str_ip not in ips:
                ips.append(str_ip)

            self.findAllIps(A, ips, first_dot, second_dot, third_dot + 1)
            self.findAllIps(A, ips, first_dot, second_dot + 1, third_dot)
            self.findAllIps(A, ips, first_dot, second_dot + 1, third_dot + 1)
            self.findAllIps(A, ips, first_dot + 1, second_dot, third_dot)
            self.findAllIps(A, ips, first_dot + 1, second_dot, third_dot + 1)
            self.findAllIps(A, ips, first_dot + 1, second_dot + 1, third_dot)
            self.findAllIps(A, ips, first_dot + 1, second_dot + 1, third_dot + 1)

    def buildIp(self, a, b, c, d):
        return "%s.%s.%s.%s" % (a, b, c, d)

    def trailing(self, s):
        if s == "0":
            return 0
        else:
            result = 0
            for i in range(len(s)):
                if s[i] != "0":
                    break
                result += 1
            return result

    def isValidIp(self, a, b, c, d):

        if self.trailing(a) > 0 or len(a) > 3:
            return False

        if self.trailing(b) > 0 or len(b) > 3:
            return False

        if self.trailing(c) > 0 or len(c) > 3:
            return False

        if self.trailing(d) > 0 or len(d) > 3:
            return False

        a, b, c, d = int(a),  int(b),  int(c),  int(d)

        _max = 255
        _min = 0
        return a <= _max and b <= _max and c <= _max and d <= _max and \
               a >= _min and b >= _min and c >= _min and d >= _min

    # @param A : string
    # @return a list of strings
    def restoreIpAddresses(self, A):
        ips = []
        self.findAllIps(A, ips, 1, 2, 3)
        return sorted(ips)
