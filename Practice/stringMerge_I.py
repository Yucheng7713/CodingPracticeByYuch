# By given two strings, merge them by overriding the common suffix and prefix
# For example : string1 = abcdfe, string2 = dfegza
# the merged result will be abcgza

def stringMerge_I(str_1, str_2):
    L = len(str_2)
    while L > 0:
        common_str = str_2[:L]
        if str_1.endswith(common_str):
            break
        L -= 1
    return str_1 + str_2[L:]

print(stringMerge_I('', 'b'))