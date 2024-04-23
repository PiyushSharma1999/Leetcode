s = "A man, a plan, a cannal: Panama"

s = s.lower()

s = ''.join(char for char in s if char.isalnum())

l, r = 0, len(s)-1

while l < r:
    if s[l] != s[r]:
        print(False)
    l+=1
    r-=1
print(True)