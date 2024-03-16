class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        ones = 0
        zer = 0

        for num in students:
          if num == 0:
            zer += 1
          else:
            ones += 1
        
        for sand in sandwiches:
          if sand == 0:
            if zer == 0:
              return ones
            zer -= 1
          if sand == 1:
            if ones == 0:
              return zer
            ones -= 1
        return 0
        
# the order doesnt matter. only if there are kids left of each type once you hit a blocking point
# once one side hits 0 then there will be no correct type left to keep the line moving
# we iterate through sandwiches while decrementing each type of kid. if one side reaches 0 then we return the other sides total
# we can use counter(students) and return counter.total() after we decrement 
    # or we can keep a total of each student type , loop through and decrement, and then return once we hit a catch
    # if no catch or sticking point then we return 0 since all kids got to eat
    


# 1700. Number of Students Unable to Eat Lunch
# Solved
# Easy
# Topics
# Companies
# Hint
# The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1 respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.

# The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack. At each step:

# If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue.
# Otherwise, they will leave it and go to the queue's end.
# This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

# You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the i​​​​​​th sandwich in the stack (i = 0 is the top of the stack) and students[j] is the preference of the j​​​​​​th student in the initial queue (j = 0 is the front of the queue). Return the number of students that are unable to eat.

 

# Example 1:

# Input: students = [1,1,0,0], sandwiches = [0,1,0,1]
# Output: 0 
# Explanation:
# - Front student leaves the top sandwich and returns to the end of the line making students = [1,0,0,1].
# - Front student leaves the top sandwich and returns to the end of the line making students = [0,0,1,1].
# - Front student takes the top sandwich and leaves the line making students = [0,1,1] and sandwiches = [1,0,1].
# - Front student leaves the top sandwich and returns to the end of the line making students = [1,1,0].
# - Front student takes the top sandwich and leaves the line making students = [1,0] and sandwiches = [0,1].
# - Front student leaves the top sandwich and returns to the end of the line making students = [0,1].
# - Front student takes the top sandwich and leaves the line making students = [1] and sandwiches = [1].
# - Front student takes the top sandwich and leaves the line making students = [] and sandwiches = [].
# Hence all students are able to eat.
# Example 2:

# Input: students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
# Output: 3
 