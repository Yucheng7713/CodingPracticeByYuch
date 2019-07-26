import re

class Checker:
    def containsAlphabet(self, s):
        return False if not re.search("[ A-Za-z]+", s) else True

    def containsGFollowedByZerosOrRs(self, s):
        return True if re.search("gr*", s) else False

    def containsACFollowedByBsAndQAfterB(self, s):
        return True if re.search("(ac)b+\\w*q+[^b]*$", s) else False

print(Checker().containsACFollowedByBsAndQAfterB("123acbeqjb123"))