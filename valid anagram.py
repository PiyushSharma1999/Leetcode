def valid_anagrams(s ,t):
    if len(s) != len(t):
        return False
    
    count_1, count_2 = {}, {}

    for i in range(len(s)):
        count_1[s[i]] = 1+count_1.get(s[i], 0)
        count_2[t[i]] = 1+count_2.get(t[i], 0)
    for c in count_1:
        if count_1[c] != count_2.get(c):
            return False
    return True

s,t = "piyush","ijushp"
print(valid_anagrams(s,t))

# O(1)

def valid_anagram_o1(s, t):
    return sorted(s) == sorted(t)

    
    