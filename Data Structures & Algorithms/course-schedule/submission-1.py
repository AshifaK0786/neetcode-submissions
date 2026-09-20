class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        queue = []

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        count = 0

        while queue:
            pre = queue.pop(0)
            count += 1

            for course in graph[pre]:
                indegree[course] -= 1

                if indegree[course] == 0:
                    queue.append(course)

        return count == numCourses
