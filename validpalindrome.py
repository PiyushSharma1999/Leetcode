s = "A man, a plan, a canal: Panama"

def isPalindrome(s):
    s = s.lower()
    s = ''.join(char for char in s if char.isalnum())

    l, r = 0, len(s)-1

    while l<r:
        if s[l] != s[r]:
            return False
        l+=1
        r-=1
    return True

print(isPalindrome(s))