from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Initialize the prerequisite map
        preMap = {i: [] for i in range(numCourses)}
        for crs, req in prerequisites:
            preMap[crs].append(req)
        
        # Set to track visiting nodes
        visit = set()

        def dfs(crs):
            if preMap[crs] == []:  # If no prerequisites, the course can be finished
                return True
            if crs in visit:  # Detect a cycle
                return False
            
            visit.add(crs)
            
            for req in preMap[crs]:
                if not dfs(req):  # If any prerequisite cannot be finished, return False
                    return False
            
            visit.remove(crs)  # Remove from visiting set after all checks
            preMap[crs] = []  # Mark this course as having no remaining prerequisites
            return True
        
        # Check each course
        for c in range(numCourses):
            if not dfs(c):  # If any course cannot be finished, return False
                return False
        return True  # All courses can be finished
    
# in my terms
# set a prereqmap to track courses as key and prereqs as value
# set a visit site to detect loops in adjacency list
# 
# define a dfs function
# first check if passed in crs has empty prereq value and return true
# check if crs is in visit which detects a loop
# after all that is done we loop through every prereq of the passed in course and call dfs on those
# if they all pass the base case checks of empty value list or in visit set
    # we remove from visited
    # we set this crs's preReqs to done by setting it o []
    # we return True

# make driver call on first course
# we also have to make calls on each course because some nodes may not be connected to each other
# if not dfs(crs) which means if anything returns false at any time then we know we cant do everything
#   we return false
# if not then we return True


# 207. Course Schedule
# Solved
# Medium
# Topics
# Companies
# Hint
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

 

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# Example 2:

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.