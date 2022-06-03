from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        # brute method is O(mn)

        # using math to solve, time complexity is O(nm+m)without refactor
        # Runtime: 334 ms, faster than 25.59% of Python3 online submissions for Number of Laser Beams in a Bank.
        # Memory Usage: 15.9 MB, less than 89.93% of Python3 online submissions for Number of Laser Beams in a Bank.

        
        # refactor 
        
        # Runtime: 305 ms, faster than 29.63% of Python3 online submissions for Number of Laser Beams in a Bank.
        # Memory Usage: 16.1 MB, less than 48.35% of Python3 online submissions for Number of Laser Beams in a Bank.
        '''
        count_of_1_of_row = \
            self.__calculate_count_of_1_each_row(bank)
        
        number_of_beams = \
            self.__calculate_number_of_beams(count_of_1_of_row)
        
        return number_of_beams
        '''
        # imporve math method by optimize calculate count 1 
        # Runtime: 104 ms, faster than 75.92% of Python3 online submissions for Number of Laser Beams in a Bank.
        # Memory Usage: 16 MB, less than 48.35% of Python3 online submissions for Number of Laser Beams in a Bank.

        count_of_1_of_row = \
            self.__calculate_count_of_1_each_row_2(bank)
        number_of_beams = \
            self.__calculate_number_of_beams(count_of_1_of_row)
        
        return number_of_beams


    def __calculate_count_of_1_each_row(self, bank):
        count_of_1_of_row = []
        # calculate count of 1 of each row
        for row in bank:
            tmp = 0
            for char in row:
                if char == '1':
                    tmp = tmp + 1
            if tmp != 0:
                count_of_1_of_row.append(tmp)

        return count_of_1_of_row

    def __calculate_number_of_beams(self, counts):
        # calculate number_of_beams
        number_of_beams = 0
        for index in range(0, len(counts)-1):
            number_of_beams += \
                counts[index] * counts[index+1]

        return number_of_beams



    def __calculate_count_of_1_each_row_2(self, bank):
      
        count_of_1_of_row = []
        for row in bank:
            tmp = 0
            row = row.replace('0','')
            if row:
                count_of_1_of_row.append(len(row))
        return count_of_1_of_row





