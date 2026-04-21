class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ''' if there is a cycle, it can't be finished '''

        graph = {i: [] for i in range(numCourses)}
        for node, pre in prerequisites:
            graph[pre].append(node)
        
        visiting = set()
        visited = set()
        def dfs(node):
            if node in visiting:
                return False
            if node in visited:
                return True
            visiting.add(node)
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            visiting.remove(node)
            visited.add(node)
            return True
        
        for node in graph.keys():
            if not dfs(node):
                return False
        return True

        
        