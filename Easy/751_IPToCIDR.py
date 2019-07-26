class Solution:
    # Convert ip string into decimal integer
    def ip2number(self, ip):
        numbers = list(map(int, ip.split(".")))
        n = (numbers[0]<<24) + (numbers[1]<<16) + (numbers[2]<<8) + numbers[3]
        return n
    # Convert decimal integer into ip string
    def number2ip(self,n):
        return ".".join([str(n>>24&255), str(n>>16&255),str(n>>8&255), str(n&255)])

    # Return the index of first '1' starting from right
    def ilowbit(self,x):
        for i in range(32):
            if(x & (1<<i)):
                return i
    # Return the number of covered ips
    def lowbit(self,x):
        return 1<<self.ilowbit(x)

    def ipToCIDR(self, ip, n):
        number = self.ip2number(ip)
        result = []
        while n>0:
            # Get the number of covered ips starting from the given ip
            lb = self.lowbit(number)
            while lb > n:
                lb = lb//2
            n -= lb
            result.append(self.number2ip(number) + "/" + str(32-self.ilowbit(lb)))
            number += lb;
        return result


ipv4, n = "255.0.0.7", 10
print(Solution().ipToCIDR(ipv4, n))
