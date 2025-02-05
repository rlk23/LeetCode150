'''
Climbing Stairs
Easy
Determine the number of distinct ways to climb a staircase of n steps by taking either 1 or 2 steps at a time.

Example:


Input: n = 4
Output: 5
'''
def climbing_stairs(n: int) -> int:
    # Write your code here
    # it good be either 1 or 2 
    if n == 0 or n==1:
        return 1
    
    return climbing_stairs(n-1) + climbing_stairs(n-2)
