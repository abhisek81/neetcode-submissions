class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] #we will append only opening characters to this stack
        hash = { ")" : "(" , "]" : "[" , "}":"{" }

        for i in range(len(s)):
            if s[i] in hash:
                if stack and stack[-1] == hash[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        return not stack