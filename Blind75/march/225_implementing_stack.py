class MyStack(object):

    def __init__(self):
        self.q = deque()
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        for i in range(len(self.q) -1):
          self.push(self.q.popleft())
        return self.q.popleft()
        

    def top(self):
        """
        :rtype: int
        """
        return self.q[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.q) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


# we are implementing queues to imitate stack
# create a deque which is a double side queue
    # push() is just appending value. will work the same on both DS
    # top you just return back of the queue since stack's top if the top but queue's top is the last
    # for empty we just return if len of q is 0
    # pop is the hardest. we need to pop out everything in the queue except the last value. as we pop we append to the back
    # this will get us the "top of the stack" which is the back of the queue
    # we use popleft to pop the left of the queue
    # return that 






# 225. Implement Stack using Queues
# Solved
# Easy
# Topics
# Companies
# Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

# Implement the MyStack class:

# void push(int x) Pushes element x to the top of the stack.
# int pop() Removes the element on the top of the stack and returns it.
# int top() Returns the element on the top of the stack.
# boolean empty() Returns true if the stack is empty, false otherwise.
# Notes:

# You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
# Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
 

# Example 1:

# Input
# ["MyStack", "push", "push", "top", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 2, 2, false]

# Explanation
# MyStack myStack = new MyStack();
# myStack.push(1);
# myStack.push(2);
# myStack.top(); // return 2
# myStack.pop(); // return 2
# myStack.empty(); // return False