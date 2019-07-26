class Solution:
    ### DFS backtracking : Recursively explore valid IPs and store them in a list
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def searchValidIPs(s, results, depth):
            # Find the rightmost '.' index for starting dividing
            right = s.rfind('.') + 1
            # The string has been divided into 4 sections : check the last section
            if depth == 3:
                if (s[right:][0] != '0' and int(s[right:]) <= 255) or (s[right:] == '0'):
                    results.append(s)
                return
            for i in range(right + 1, right + 4):
                if i >= len(s): continue
                # Form a candidate IP by dividing a chunk of section
                cand_ip = s[:i] + '.' + s[i:]
                # Check if the chunk is valid or not -> if it is valid : do the next dividing
                if (s[right:i][0] != '0' and int(s[right:i]) <= 255) or s[right:i] == '0':
                    searchValidIPs(cand_ip, results, depth+1)
        ips = []
        searchValidIPs(s, ips, 0)
        return ips

    ### OMG solution
    def restoreIpAddresses_II(self, s):
        res = []
        r = [1, 2, 3]
        for a in r:
            for b in r:
                for c in r:
                    for d in range(1, 4):
                        if a + b + c + d != len(s): continue
                        ip_str = [s[:a], s[a:a + b], s[a + b:a + b + c], s[a + b + c:]]
                        ip_int = [int(ip) for ip in ip_str if int(ip) < 256]
                        if len(ip_int) != 4: continue
                        ip_str_without_prefix = [str(ip) for ip in ip_int]
                        if ip_str != ip_str_without_prefix: continue
                        res.append(".".join(ip_str))
        return res

ip_str = "010010"
print(Solution().restoreIpAddresses(ip_str))