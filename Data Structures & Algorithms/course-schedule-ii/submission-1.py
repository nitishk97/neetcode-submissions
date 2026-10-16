class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        prereq = {i:[] for i in range(numCourses)} # prerequisite -> list of courses
        queue = deque()
        indegree = [0]*numCourses #Number of prereq for a course
        for course, pre in prerequisites:
            prereq[pre].append(course)
            indegree[course]+=1

        for course in range(numCourses):
            if indegree[course]==0:
                queue.append(course)
        course_taken = []
        while queue:
            course = queue.popleft()
            course_taken.append(course)
            for c in prereq[course]:
                indegree[c]-=1
                if indegree[c]==0:
                    queue.append(c)
        if len(course_taken)==numCourses:
            return course_taken
        return []
