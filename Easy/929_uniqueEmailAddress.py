class Solution:
    def numUniqueEmails(self, emails):
        results = set()
        for email in emails:
            e = email.split('@')
            local_name = e[0].replace('.','').split('+')[0]
            results.add(local_name + '@' + domain_name)
        return len(list(results))