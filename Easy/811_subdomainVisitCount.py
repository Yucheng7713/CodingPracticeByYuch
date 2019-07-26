class Solution:
    def getAllSubDomains(self, domainStr):
        d_str, results = "", []
        subdomains = domainStr.split('.')[::-1]
        for sub_d in subdomains:
            d_str = sub_d + d_str
            results.append(d_str);
            d_str = '.' + d_str
        return results

    def subdomainVisits(self, cpdomains):
        results = []
        cp_map = dict()
        for cp in cpdomains:
            count, domain = int(cp.split(' ')[0]), cp.split(' ')[1]
            sub_domains = self.getAllSubDomains(domain)
            for sub_d in sub_domains:
                if cp_map.get(sub_d) is None:
                    cp_map[sub_d] = 0
                cp_map[sub_d] += count

        for key, value in cp_map.items():
            results.append(str(value) + " " + key)

        return results

s = Solution()

domains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
print(s.subdomainVisits(domains))