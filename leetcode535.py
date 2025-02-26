'''
Note: This is a companion problem to the System Design problem: Design TinyURL.
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk. Design a class to encode a URL and decode a tiny URL.

There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

Implement the Solution class:

Solution() Initializes the object of the system.
String encode(String longUrl) Returns a tiny URL for the given longUrl.
String decode(String shortUrl) Returns the original long URL for the given shortUrl. It is guaranteed that the given shortUrl was encoded by the same object.
 

Example 1:

Input: url = "https://leetcode.com/problems/design-tinyurl"
Output: "https://leetcode.com/problems/design-tinyurl"

Explanation:
Solution obj = new Solution();
string tiny = obj.encode(url); // returns the encoded tiny url.
string ans = obj.decode(tiny); // returns the original url after decoding it.
 

Constraints:

1 <= url.length <= 104
url is guranteed to be a valid URL.

'''

import random
import string

class Codec:
    def __init__(self):
        self.long_to_short = {}  # Maps long URL -> short URL
        self.short_to_long = {}  # Maps short URL -> long URL
        self.base_url = "http://tinyurl.com/"

    def _generate_short_key(self):
        """Generates a random 6-character short key using Base62 encoding."""
        chars = string.ascii_letters + string.digits  # a-z, A-Z, 0-9
        return ''.join(random.choices(chars, k=6))  # Generate a random 6-character string
    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        if longUrl in self.long_to_short:
            return self.base_url + self.long_to_short[longUrl]  # Return existing short URL
        
        short_key = self._generate_short_key()
        
        # Ensure uniqueness of short key
        while short_key in self.short_to_long:
            short_key = self._generate_short_key()
        
        # Store mappings
        self.long_to_short[longUrl] = short_key
        self.short_to_long[short_key] = longUrl
        
        return self.base_url + short_key  # Return full short URL
    
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        short_key = shortUrl.replace(self.base_url, "")  # Extract short key
        return self.short_to_long.get(short_key, "")  # Return original long URL or empty string
