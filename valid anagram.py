def valid_anagrams(input_string_1 ,input_string_2):
    if len(input_string_1) != len(input_string_2):
        return False
    
    count_1, count_2 = {}, {}

    for i in range(len(input_string_1)):
        count_1[input_string_1[i]] = 1+count_1.get(input_string_1[i], 0)
        count_2[input_string_2[i]] = 1+count_2.get(input_string_2[i], 0)
    for c in count_1:
        if count_1[c] != count_2.get(c):
            return False
    return True

s,t = "piyush","ijushp"
print(valid_anagrams(s,t))

# O(1)

def valid_anagram_o1(s, t):
    return sorted(s) == sorted(t)

    
    