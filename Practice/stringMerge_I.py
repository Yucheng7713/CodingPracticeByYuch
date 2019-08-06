def stringMerge_I(str_1, str_2):
    L = len(str_2)
    while L > 0:
        common_str = str_2[:L]
        if str_1.endswith(common_str):
            break
        L -= 1
    return str_1 + str_2[L:]

print(stringMerge_I('', 'b'))