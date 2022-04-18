# Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end to hold the additional characters,
# and that you are given the 'true'length of the string.

# !! Since string in Python is immutable, here doesn't do the replacement in place.

def stringURLify(str):
    url_str = ""
    for c in str.strip():
        if c != " ":
            url_str += c
        else:
            url_str += "%20"
    return url_str

if __name__ == '__main__':
    print(stringURLify("Mr John Smith     "))

