class Solution:
    # Brute Force Cancatenation - Bad Performance
    def helper(self, nums):
        eng_num = []
        one_digit = { '0':'Zero', '1':'One', '2':'Two', '3':'Three', '4':'Four', '5':'Five', '6':'Six', '7':'Seven', '8':'Eight', '9':'Nine'}
        two_digit_1 = { '0':'Ten', '1':'Eleven', '2':'Twelve', '3':'Thirteen', '4':'Fourteen', '5':'Fifteen', '6':'Sixteen', '7':'Seventeen', '8':'Eighteen', '9':'Nineteen'}
        two_digit_N = { '2':'Twenty', '3':'Thirty', '4':'Forty', '5':'Fifty', '6':'Sixty', '7':'Seventy', '8':'Eighty', '9':'Ninety'}
        mega = ["Thousand", "Million", "Billion"]
        mega_index = 0
        for i in range(len(nums)-1, -1, -1):
            k = nums[i]
            temp = []
            if len(k) > 2:
                if k[0] != '0':
                    temp += [one_digit[k[0]]+" Hundred"]
                k = k[1:]
            if len(k) > 1:
                if k[0] == '1':
                    temp += [two_digit_1[k[1]]]
                    k = ""
                elif k[0] != '0':
                    temp += [two_digit_N[k[0]]]
                k = k[1:]
            if len(k) > 0:
                if k[0] != '0':
                    temp += [one_digit[k[0]]]
            if i > 0 and int(nums[i-1]) > 0:
                temp = [mega[mega_index]] + temp
            mega_index += 1
            eng_num = temp + eng_num
        return " ".join(eng_num) if len(eng_num) > 0 else "Zero"
    def numberToWords(self, num: int) -> str:
        num = str(num)
        group, digits = [], ""
        for i in range(len(num)-1, -1, -1):
            digits = num[i] + digits
            if len(digits) == 3:
                group += [digits]
                digits = ""
        if len(digits) > 0:
            group.append(digits)
        return self.helper(group[::-1])

n = 12345
print(Solution().numberToWords(n))