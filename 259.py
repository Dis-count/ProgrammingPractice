"""
@Author      :   Discount 
@Time        :   08/12/2022 13:19:56
@Description :   
"""

# 1812. Determine Color of a Chessboard Square
# 简单
# You are given coordinates, a string that represents the coordinates of a square of the chessboard. Below is a chessboard for your reference.


# Return true if the square is white, and false if the square is black.

# The coordinate will always represent a valid chessboard square. The coordinate will always have the letter first, and the number second. 

# Example 1:

# Input: coordinates = "a1"
# Output: false
# Explanation: From the chessboard above, the square with coordinates "a1" is black, so return false.

# Example 2:

# Input: coordinates = "h3"
# Output: true
# Explanation: From the chessboard above, the square with coordinates "h3" is white, so return true.

# Example 3:

# Input: coordinates = "c7"
# Output: false

# chr(number) vs ord(character)

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        res = ord(coordinates[0])-ord('a') + int(coordinates[1])
        if int(res)%2:
            return False
        else:    
            return True

coordinates = "a1"

s = Solution()
s.squareIsWhite(coordinates)