
# Use 6-digit alphabets to mapping the long URL
# the 6-digit codes can provide
# (10 + 26 + 26)^6 sets of URL which is quite enough
class Codec:

    alphabet_set = string.ascii_letters + '0123456789'

    def __init__(self):
        self.urlToCode = dict()
        self.codeToUrl = dict()

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        while longUrl not in self.urlToCode:
            url_code = ''.join(random.choice(Codec.alphabet_set) for i in range(6))
            if url_code not in self.codeToUrl:
                self.urlToCode[longUrl] = url_code
                self.codeToUrl[url_code] = longUrl
        return "https://tinyurl.com/" + self.urlToCode[longUrl]

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        url_code = shortUrl.split('/')[-1]
        if url_code in self.codeToUrl:
            return self.codeToUrl[url_code]
        return ""

        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.decode(codec.encode(url))