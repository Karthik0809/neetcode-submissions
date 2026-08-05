class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        in_deg = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_deg[course] += 1

        queue = deque([i for i in range(numCourses) if in_deg[i] == 0])
        count = 0

        while queue:
            course = queue.popleft()
            count += 1
            for next_course in graph[course]:
                in_deg[next_course] -= 1
                if in_deg[next_course] == 0:
                    queue.append(next_course)

        return count == numCourses