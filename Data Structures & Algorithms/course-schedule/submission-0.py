from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = defaultdict(list)
        q = deque([])

        for dest, src in prerequisites:
            indegree[dest] += 1
            adj[src].append(dest)
        
        for course, prereqs in enumerate(indegree):
            if prereqs == 0:
                q.append(course)

        courses_left = numCourses
        while q:
            cur = q.popleft()
            courses_left -= 1
            for neighbor in adj[cur]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        return courses_left == 0
