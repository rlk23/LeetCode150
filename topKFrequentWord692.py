'''
Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

 

Example 1:

Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:

Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.
 

Constraints:

1 <= words.length <= 500
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
k is in the range [1, The number of unique words[i]]
 

Follow-up: Could you solve it in O(n log(k)) time and O(n) extra space?

'''

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hashMap = {}

        for word in words:
            if word in hashMap:
                hashMap[word] += 1
            else:
                hashMap[word] = 1

        max_freq = max(hashMap.values())
        buckets = [[] for _ in range(max_freq+1)]

        for word, count in hashMap.items():
            buckets[count].append(word)
        # Step 4: Sort each bucket lexicographically
        for bucket in buckets:
            bucket.sort()

        # Step 5: Collect results in order of frequency
        result = []
        for freq in range(max_freq, 0, -1):
            for word in buckets[freq]:
                result.append(word)
                if len(result) == k:  # Stop when we've collected k words
                    return result

                    

