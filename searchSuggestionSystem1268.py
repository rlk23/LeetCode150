'''
You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of searchWord is typed.

 

Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"].
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"].
After typing mou, mous and mouse the system suggests ["mouse","mousepad"].
Example 2:

Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
Explanation: The only word "havana" will be always suggested while typing the search word.
 

Constraints:

1 <= products.length <= 1000
1 <= products[i].length <= 3000
1 <= sum(products[i].length) <= 2 * 104
All the strings of products are unique.
products[i] consists of lowercase English letters.
1 <= searchWord.length <= 1000
searchWord consists of lowercase English letters.

'''
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isAtEnd = False
        self.words = []  # Store words at each node for suggestions

class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def add_node(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            # Maintain a sorted list of words at each node
            curr.words.append(word)
            curr.words.sort()
            if len(curr.words) > 3:  # Keep only top 3 lexicographically
                curr.words.pop()
        curr.isAtEnd = True
    
    def get_suggestions(self, prefix):
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return []  # No suggestions for this prefix
            curr = curr.children[c]
        return curr.words  # Return stored suggestions
    
    def suggestedProducts(self, products, searchWord):
        # Add words to the Trie
        for word in sorted(products):  # Sort products to handle lexicographical order
            self.add_node(word)
        
        # Collect suggestions for each prefix of searchWord
        res = []
        prefix = ""
        for c in searchWord:
            prefix += c
            res.append(self.get_suggestions(prefix))
        return res


