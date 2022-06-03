from typing import List
import math

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        # do it in two stage, flip stage and inver stage
        # time complexity is O(n)
        # Runtime: 40 ms, faster than 99.88% of Python3 online submissions for Flipping an Image.
        # Memory Usage: 13.8 MB, less than 65.23% of Python3 online submissions for Flipping an Image.

        image = self.__flip_stage(image)
        image = self.__invert_stage(image)

        return image

    def __flip_stage(self, image):
        length = len(image[0]) 

        for row in image:
            for index in range(0, math.floor(length/2)):
                '''
                list reverse just do it 
                when index is equal half of list
                '''
                # swap 
                row[index], row[length-index-1] = \
                    row[length-index-1], row[index]
        return image

    def __invert_stage(self, image):
        # invert stage
        length = len(image[0]) 
        for row in image:
            for index in range(0, length):
                if row[index] == 1:
                    row[index] = 0
                elif row[index] == 0:
                    row[index] = 1

        return image




