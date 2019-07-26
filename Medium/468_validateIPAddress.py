class Solution:
    # IPv4 validation check
    def validIPv4(self, ipv4s):
        return all(re.match('^[0-9]+$', ip) and int(ip) <= 255 and int(ip) >= 0 and ip == str(int(ip)) for ip in ipv4s)

    # IPv6 validation check
    def validIPv6(self, ipv6s):
        hex_set = '0123456789abcdefABCDEF'
        return all(len(ip) >= 1 and len(ip) <= 4 and all(c in hex_set for c in ip) for ip in ipv6s)


    def validIPAddress(self, IP: str) -> str:
        if IP.count('.') == 3 and self.validIPv4(IP.split('.')):
            return "IPv4"
        elif IP.count(':') == 7 and self.validIPv6(IP.split(':')):
            return "IPv6"
        return "Neither"