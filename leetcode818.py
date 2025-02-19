'''
Your car starts at position 0 and speed +1 on an infinite number line. Your car can go into negative positions. Your car drives automatically according to a sequence of instructions 'A' (accelerate) and 'R' (reverse):

When you get an instruction 'A', your car does the following:
position += speed
speed *= 2
When you get an instruction 'R', your car does the following:
If your speed is positive then speed = -1
otherwise speed = 1
Your position stays the same.
For example, after commands "AAR", your car goes to positions 0 --> 1 --> 3 --> 3, and your speed goes to 1 --> 2 --> 4 --> -1.

Given a target position target, return the length of the shortest sequence of instructions to get there.

 

Example 1:

Input: target = 3
Output: 2
Explanation: 
The shortest instruction sequence is "AA".
Your position goes from 0 --> 1 --> 3.
Example 2:

Input: target = 6
Output: 5
Explanation: 
The shortest instruction sequence is "AAARA".
Your position goes from 0 --> 1 --> 3 --> 7 --> 7 --> 6.
 
'''

class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1, 0)])  # (position, speed, moves)
        visited = set((0, 1))  # Track visited (position, speed)

        while queue:
            pos, speed, moves = queue.popleft()

            if pos == target:
                return moves
            
            next_pos, next_speed = pos + speed, speed * 2
            if (next_pos, next_speed) not in visited and 0 <= next_pos <= 2 * target:   
                visited.add((next_pos,next_speed))
                queue.append((next_pos, next_speed, moves +1))

            reverse_speed = -1 if speed > 0 else 1
            if (pos, reverse_speed) not in visited:
                visited.add((pos, reverse_speed))
                queue.append((pos, reverse_speed, moves + 1))
