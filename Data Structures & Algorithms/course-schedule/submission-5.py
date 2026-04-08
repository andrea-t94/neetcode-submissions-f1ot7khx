class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ''' if there is a cycle, it can't be finished '''

        graph = {i: [] for i in range(numCourses)} #crs, [prereqs]
        for a, b in prerequisites:
            graph[a].append(b)
        print(graph)
        
        visited = set() #it means that node is good
        visiting = set()
        #there is a cycle if I go back to a node that I am visiting already
        def dfs(node):
            if node in visited:
                return True
            if node in visiting:
                return False
            
            visiting.add(node) 
            for pre in graph[node]:
                if not dfs(pre):
                    return False
            # after I've checked node, I mark it as good
            visiting.remove(node)
            visited.add(node)
            return True
        for node in graph.keys():
            if not dfs(node):
                return False
        return True

            
