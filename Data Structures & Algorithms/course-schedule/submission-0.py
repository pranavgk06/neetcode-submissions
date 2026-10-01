class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i : [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adj[prereq].append(course)
        
        state = [0] * numCourses

        def dfs(node):
            if state[node] == 1:
                return False
            if state[node] == 2:
                return True
            
            state[node] = 1

            for neighbor in adj[node]:
                if not dfs(neighbor):
                    return False
            
            state[node] = 2
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True