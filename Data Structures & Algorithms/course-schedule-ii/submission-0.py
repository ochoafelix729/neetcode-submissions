from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = defaultdict(list)
        q = deque([])

        for dest, src in prerequisites:
            indegree[dest] += 1
            adj[src].append(dest)

        for course, num_prereqs in enumerate(indegree):
            if num_prereqs == 0:
                q.append(course)

        ordering = []
        while q:
            cur = q.popleft()
            ordering.append(cur)
            for neighbor in adj[cur]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        if len(ordering) == numCourses:
            return ordering
        
        return []
