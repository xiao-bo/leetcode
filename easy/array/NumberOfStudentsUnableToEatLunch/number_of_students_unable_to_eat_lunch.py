from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        # using stack 
        # Runtime: 61 ms, faster than 33.41% of Python3 online submissions for Number of Students Unable to Eat Lunch.
        # Memory Usage: 13.9 MB, less than 21.62% of Python3 online submissions for Number of Students Unable to Eat Lunch.
        '''
        stop = len(students)
        retry_count = 0

        while retry_count < stop:
            student = students.pop(0) # 移除queue第一位學生
        
            if student == sandwiches[0]:
                
                sandwiches.pop(0) # 移除stack最上層
                retry_count = 0 # 有學生拿到，重新計算終止條件
                stop = len(students)
            else:
                students.append(student) # 重新排隊
                retry_count += 1
        
        return len(students)
        '''
        # improve stack method
        # Runtime: 41 ms, faster than 79.58% of Python3 online submissions for Number of Students Unable to Eat Lunch.
        # Memory Usage: 13.8 MB, less than 98.36% of Python3 online submissions for Number of Students Unable to Eat Lunch.
        
        retry_count = 0
        while students:
        
            if students[0] == sandwiches[0]:
                students.pop(0) # 移除queue第一位學生
                sandwiches.pop(0) # 移除stack最上層
                retry_count = 0 # 有學生拿到，重新計算終止條件
                
            else:
                students.append(students.pop(0)) # 重新排隊
                retry_count += 1

            if retry_count >=len(students):
                break 

        return len(students)


