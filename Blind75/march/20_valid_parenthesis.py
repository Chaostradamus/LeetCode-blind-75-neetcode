class Solution(object):
    def isValid(self, s):
      # stack = []
      # for c in s:
      #   if c in "({[":
      #     stack.append(c)
      #   if not stack or \
      #     (c == ')' and stack[-1] != '(') or\
      #     (c == ']' and stack[-1] != '[') or\
      #     (c == '}' and stack[-1] != '{'):
      #     return False
      #   stack.pop
      # return stack
      
      stack = []
      for c in s:
        if c in "({[":
          stack.append(c)
        if not stack or \
          (c == ")" and stack[-1] != "(") or \
          (c == "}" and stack[-1] != "{") or \
          (c == "]" and stack[-1] != "["):
          return False
        stack.pop()
      return stack
    
# create a stack
# append to stack if its an open bracket
# else if its a closed bracket and the top of the stack wasnt the corresponding opening bracker
# return false
# otherwise pop that set of brackets
# return stack at end

# can also use hashset to check each paren to correct mapping
# o(n) space and time