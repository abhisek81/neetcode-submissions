class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash = { "]" : "[" , "}" : "{" , ")" : "(" }

        for ch in s:
            if ch in hash:
                if stack and hash[ch] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        
        #return not stack
        if stack == []:
            return True
        else:
            return False
