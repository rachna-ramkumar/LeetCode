class Solution:
    def isValid(self, s: str) -> bool:
        #initialize the stack
        stack = []
        #create a hashmap to keep track of the opening and closing brackets
        mapping = { ')' : '(' , '}' : '{' , ']' : '[' }
        #for each character in the input
        for char in s:
            #check if it is a closing bracket
            if char in mapping:
                #check the top element of the stack if there is any present, if not, return #
                top_element = stack.pop() if stack else '#'
                # check if the top most element of the stack is an opening bracket for the closing bracket. IF not, return false.
                if mapping[char] != top_element: 
                    return False
            else:
                #it is an opening bracket
                stack.append(char)
        #return if there is no stack. IF there is no stack, then it is a valid parenthesis. Else, it is not.
        return not stack

    #Time Complexity Analysis:
    #O(n)
    #Space Complexity Analysis:
    #O(n)
                    
                
        