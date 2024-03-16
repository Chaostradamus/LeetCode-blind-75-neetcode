class MinStack(object):

    def __init__(self):
      self.stack = []
      self.minStack = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
        
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.minStack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
    


#     155. Min Stack
# Solved
# Medium
# Topics
# Companies
# Hint
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

 

# Example 1:

# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2
    

# first initialize s stack and minimum stack. one as the main stack and one to hold the minimum at the currently pushed value
# top and getMin are just peeks at the top of the respective stacks
# pop is just popping off both stacks
# push is the most invovled operation
#     you pul the val onto stack. you also have to take the minimum between current value and previous minimum
#     if you push 6, 24, 3. push 6..minstack empty so minval is also 6
#     push 24... val is 24 and prev minimum is 6 so 24 gets pushed onto stack BUT 6 gets pushed onto min stack
#     when you push the 3. stack gets 3 like usual. min stack gets minimum between 3 and top of minstack which is 6. so min stack gets 3
#     if you pop then 3 gets popped off both stacks and minimum will revert back to 6. if you popped a larger number then the 3 remains the min