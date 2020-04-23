class Solution():

    def remove(self, ips):

        # O(n2) = 2 for loops

        # 2nd O(n log n) = sorting

        ips = sorted([(ip, idx) for idx, ip in enumerate(ips)], key=lambda k: (k[0], k[1]))

        i = 0
        while i < len(ips) and i + 1 < len(ips):
            current = ips[i]
            next = ips[i+1]

            if next[0] == current[0]:
                del ips[i + 1]
            else:
                i += 1

        # reconstruct initial order
        return [ip[0] for ip in sorted(ips, key=lambda k: k[1])]

print(Solution().remove(["103", "233", "116", "103", "50", "89", "103", "116"]))
