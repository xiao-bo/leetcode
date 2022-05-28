from typing import List
import math

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        # do it in two stage, flip stage and inver stage
        # time complexity is O(n)
        # Runtime: 40 ms, faster than 99.88% of Python3 online submissions for Flipping an Image.
        # Memory Usage: 13.8 MB, less than 65.23% of Python3 online submissions for Flipping an Image.

        # flip stage 

        # I put it before loop because image is square,
        # so length of row of image is same
        # therefore put it before loop will reduce unuseful declare time
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

        # invert stage

        for row in image:
            for index in range(0, length):
                if row[index] == 1:
                    row[index] = 0
                elif row[index] == 0:
                    row[index] = 1

        return image




