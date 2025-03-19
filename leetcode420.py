'''
A password is considered strong if the below conditions are all met:

It has at least 6 characters and at most 20 characters.
It contains at least one lowercase letter, at least one uppercase letter, and at least one digit.
It does not contain three repeating characters in a row (i.e., "Baaabb0" is weak, but "Baaba0" is strong).
Given a string password, return the minimum number of steps required to make password strong. if password is already strong, return 0.

In one step, you can:

Insert one character to password,
Delete one character from password, or
Replace one character of password with another character.
 

Example 1:

Input: password = "a"
Output: 5
Example 2:

Input: password = "aA1"
Output: 3
Example 3:

Input: password = "1337C0d3"
Output: 0
 

Constraints:

1 <= password.length <= 50
password consists of letters, digits, dot '.' or exclamation mark '!'.

'''


class Solution(object):
    def strongPasswordChecker(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Step 1: Determine missing character types (lowercase, uppercase, digit)
          missing_type = 3  # Assume all 3 types are missing
        if any('a' <= c <= 'z' for c in s): missing_type -= 1  # Contains a lowercase letter
        if any('A' <= c <= 'Z' for c in s): missing_type -= 1  # Contains an uppercase letter
        if any(c.isdigit() for c in s): missing_type -= 1# Contains a digit

        # Step 2: Detect repeating sequences (3 or more consecutive characters)
        change = 0  # Track replacements needed to fix repeating sequences
        one = two = 0  # one: Sequences where length % 3 == 0, two: length % 3 == 1
        p = 2  # Start checking from the third character

        while p < len(s):
            # If three consecutive characters are the same, count the length of the repeating sequence
            if s[p] == s[p-1] == s[p-2]:
                length = 2  # Minimum length of a repeating sequence
                while p < len(s) and s[p] == s[p-1]:  # Count consecutive same characters
                    length += 1
                    p += 1
                    
                # Every group of 3 requires at least 1 replacement
                change += length // 3  

                # Categorize the sequence based on its length % 3 value
                if length % 3 == 0:  
                    one += 1  # 3n-length sequences (best removed with 1 deletion)
                elif length % 3 == 1:  
                    two += 1  # 3n+1-length sequences (best removed with 2 deletions)
            else:
                p += 1  # Move to the next character
        
        # Step 3: Handle different cases based on password length

        # Case 1: If password is too short (< 6), return the max of missing types or characters to be added
        if len(s) < 6:
            return max(missing_type, 6 - len(s))

        # Case 2: If password length is valid (6 ≤ len ≤ 20), return max of missing character types or required changes
        elif len(s) <= 20:
            return max(missing_type, change)

        # Case 3: If password is too long (> 20), excess characters need to be removed
        else:
            delete = len(s) - 20  # Number of deletions required to shorten the password

            # Prioritize removing characters from one-sequence groups (length % 3 == 0)
            change -= min(delete, one)
            
            # Then remove from two-sequence groups (length % 3 == 1), since they need 2 deletions
            change -= min(max(delete - one, 0), two * 2) // 2
            
            # Finally, remove remaining excess characters from general repeating sequences
            change -= max(delete - one - 2 * two, 0) // 3

            # Return the total number of deletions + max(missing character types, replacements needed)
            return delete + max(missing_type, change)
