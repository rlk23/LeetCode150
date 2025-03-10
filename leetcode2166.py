'''

Code
Testcase
Testcase
Test Result
2162. Minimum Cost to Set Cooking Time
Solved
Medium
Topics
Companies
Hint
A generic microwave supports cooking times for:

at least 1 second.
at most 99 minutes and 99 seconds.
To set the cooking time, you push at most four digits. The microwave normalizes what you push as four digits by prepending zeroes. It interprets the first two digits as the minutes and the last two digits as the seconds. It then adds them up as the cooking time. For example,

You push 9 5 4 (three digits). It is normalized as 0954 and interpreted as 9 minutes and 54 seconds.
You push 0 0 0 8 (four digits). It is interpreted as 0 minutes and 8 seconds.
You push 8 0 9 0. It is interpreted as 80 minutes and 90 seconds.
You push 8 1 3 0. It is interpreted as 81 minutes and 30 seconds.
You are given integers startAt, moveCost, pushCost, and targetSeconds. Initially, your finger is on the digit startAt. Moving the finger above any specific digit costs moveCost units of fatigue. Pushing the digit below the finger once costs pushCost units of fatigue.

There can be multiple ways to set the microwave to cook for targetSeconds seconds but you are interested in the way with the minimum cost.

Return the minimum cost to set targetSeconds seconds of cooking time.

Remember that one minute consists of 60 seconds.

 
'''
class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        def calculate_cost(time_str):
            """Computes the cost of entering a given time string"""
            cost = 0
            current_digit = str(startAt)

            for digit in time_str:
                if digit != current_digit:
                    cost += moveCost  # Moving to a new digit
                    current_digit = digit
                cost += pushCost  # Pressing the digit

            return cost

        min_cost = float('inf')

        # Generate valid (minutes, seconds) representations
        for m in range(100):
            s = targetSeconds - (m * 60)
            if 0 <= s < 100:
                # Convert to a valid string without unnecessary leading zeros
                time_str = f"{m}{s:02d}".lstrip("0")

                # Ensure the total length of the time string is ≤ 4
                if 1 <= len(time_str) <= 4:
                    min_cost = min(min_cost, calculate_cost(time_str))

        return min_cost
