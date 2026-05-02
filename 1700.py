class Solution:
    def countStudents(self, students, sandwiches):
        count = [0, 0]
        
        # count student preferences
        for s in students:
            count[s] += 1
        
        for s in sandwiches:
            if count[s] == 0:
                return count[0] + count[1]
            count[s] -= 1
        
        return 0