'''
Given the coordinates of four points in 2D space p1, p2, p3 and p4, return true if the four points construct a square.

The coordinate of a point pi is represented as [xi, yi]. The input is not given in any order.

A valid square has four equal sides with positive length and four equal angles (90-degree angles).

 

Example 1:

Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: true
Example 2:

Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]
Output: false
Example 3:

Input: p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]
Output: true
 

Constraints:

p1.length == p2.length == p3.length == p4.length == 2
-104 <= xi, yi <= 104

'''

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        
        distances = [
            self.distance(p1,p2),
            self.distance(p1,p3),
            self.distance(p1,p4),
            self.distance(p2,p3),
            self.distance(p2,p4),
            self.distance(p3,p4)
        ]

        distances.sort()
        return (
            distances[0] > 0 and  # Ensures no duplicate points (zero distance)
            distances[0] == distances[1] == distances[2] == distances[3] and  # Four equal sides
            distances[4] == distances[5] and  # Two equal diagonals
            2 * distances[0] == distances[4]  # Diagonal follows the Pythagorean theorem
        )



    
    def distance(self,v1, v2):
        return (v1[0] - v2[0])**2 + (v1[1] - v2[1])**2

