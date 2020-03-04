class Maximal:
    def lengthOfLongestSubstring(self, c):
        if len(c) > 0:
            substring = c[0]
            seq = 1
        else:
            return 0
        for i in range(1, len(c)):
            if c[i] not in substring:
                substring = substring + c[i]
            else:
                seq = max(len(substring), seq)
                ind = substring.find(c[i])
                substring = substring[ind+1:len(substring)] + c[i]

        seq = max(len(substring), seq)
        return seq


test = Maximal()
t=input('');

output = test.lengthOfLongestSubstring(t)
print(format(output))