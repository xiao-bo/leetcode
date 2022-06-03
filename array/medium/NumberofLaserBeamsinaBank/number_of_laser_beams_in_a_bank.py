from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        # brute method is O(mn)

        # using math to solve, time complexity is
        # Runtime: 334 ms, faster than 25.59% of Python3 online submissions for Number of Laser Beams in a Bank.
        # Memory Usage: 15.9 MB, less than 89.93% of Python3 online submissions for Number of Laser Beams in a Bank.

        number_of_beams = 0
        count_of_1_of_row = []
        # calculate count of 1 of each row
        for row in bank:
            tmp = 0
            for char in row:
                if char == '1':
                    tmp = tmp + 1

            if tmp != 0:
                count_of_1_of_row.append(tmp)

        # calculate number_of_beams
        for index in range(0, len(count_of_1_of_row)-1):
            number_of_beams += \
                count_of_1_of_row[index] * count_of_1_of_row[index+1]

        return number_of_beams
