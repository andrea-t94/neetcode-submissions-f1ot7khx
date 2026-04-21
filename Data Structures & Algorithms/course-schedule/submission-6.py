class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ''' if there is a cycle, it can't be finished '''

        graph = {i: [] for i in range(numCourses)}
        indegree = [0]*numCourses
        for node, pre in prerequisites:
            graph[pre].append(node)
            indegree[node] += 1
        
        q = deque()
        for node in graph.keys():
            if indegree[node] == 0:
                q.append(node)
        
        cnt = 0
        while q:
            node = q.popleft()
            cnt += 1
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return cnt == numCourses


            
