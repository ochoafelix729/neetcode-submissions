class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adjList = defaultdict(list)

        for course, prereq in prerequisites:
            indegree[course] += 1
            adjList[prereq].append(course)

        
        q = deque([])
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
                numCourses -=1 
        
        while q:
            cur = q.popleft()
            for nei in adjList[cur]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
                    numCourses -= 1
        return numCourses == 0
            
        
