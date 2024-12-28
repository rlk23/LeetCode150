'''
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0


'''

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        checkDict = {"b":1, "a": 1, "l":2,"o":2, "n": 1}

        dictIt = {}


        textCounter = Counter(text)

        return min(textCounter[char] // count for char, count in checkDict.items())

