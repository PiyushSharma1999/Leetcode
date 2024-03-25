class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p_map ={
                    "}":"{",
                    "]":"[",
                    ")":"("
                } 
        stack =[]
        for c in s:
            if c in p_map:
                if stack[-1] == p_map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

s = "()[]{}"

meth = Solution()

print(meth.isValid(s))

# Create map and empty stack -> iterate ove string. Check if current item is a key in the map if not append the item to stack. If it is present then check if
# the last item in the stack is equal to the value of that key and pop item else retuen false.
