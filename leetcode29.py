'''
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

 

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.
 

Constraints:

-231 <= dividend, divisor <= 231 - 1
divisor != 0
'''
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
            # Handle edge case of overflow
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1  # Clamping to 32-bit integer max limit
        
        # Determine the sign of the result
        negative = (dividend < 0) != (divisor < 0)  # XOR operation to check sign

        # Work with absolute values
        dividend, divisor = abs(dividend), abs(divisor)
        
        quotient = 0
        # Shift divisor left until it is the largest multiple <= dividend
        while dividend >= divisor:
            temp_divisor, multiple = divisor, 1
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1  # Double the divisor
                multiple <<= 1  # Double the corresponding quotient part
            
            # Subtract the largest possible multiple from the dividend
            dividend -= temp_divisor
            quotient += multiple
        
        # Apply sign to the quotient
        return -quotient if negative else quotient
