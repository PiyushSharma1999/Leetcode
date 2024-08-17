s = "AABABBA"
k = 1

def longRepeatCharReplace(s, k):
    count = {}
    maxf = 0
    l = 0

    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        maxf = max(maxf, count[s[r]])

        if (r - l + 1) - maxf > k:
            count[s[l]] -= 1
            l += 1
    return (r - l + 1)


print(longRepeatCharReplace(s, k))