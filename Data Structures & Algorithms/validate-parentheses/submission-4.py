class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] #we will append only opening characters to this stack
        hash = { ")" : "(" , "]" : "[" , "}":"{" }

        #read the 1st character from string
        for ch in s:  
            #check if it's in hash means check if it's a closing character
            if ch in hash:  
                if stack and stack[-1] == hash[ch]:
                    stack.pop() 
                else:
                    return False 
            #if it is not a closing character then it is a opening character, 
            #so append to stack          
            else:
                stack.append(ch)
        #if not stack:
        #    return True
        #else:
        #    return False
        return not stack