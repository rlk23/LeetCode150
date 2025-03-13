'''
Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:

LFUCache(int capacity) Initializes the object with the capacity of the data structure.
int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.

The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

Explanation
// cnt(x) = the use counter for key x
// cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // return 1
                 // cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                 // cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                 // cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      // return 4
                 // cache=[4,3], cnt(4)=2, cnt(3)=3

'''

from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_value_map = {}  # Stores key -> value
        self.key_freq_map = {}   # Stores key -> frequency
        self.freq_list_map = defaultdict(OrderedDict)  # Stores frequency -> {key: None} (OrderedDict maintains LRU order)

    def get(self, key: int) -> int:
        if key not in self.key_value_map or self.capacity == 0:
            return -1
        
        # Update frequency
        self._update_frequency(key)
        return self.key_value_map[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        if key in self.key_value_map:
            self.key_value_map[key] = value
            self._update_frequency(key)
        else:
            if len(self.key_value_map) == self.capacity:
                self._evict_least_frequent()

            # Insert new key with frequency 1
            self.key_value_map[key] = value
            self.key_freq_map[key] = 1
            self.freq_list_map[1][key] = None
            self.min_freq = 1  # Reset min frequency to 1

    def _update_frequency(self, key):
        freq = self.key_freq_map[key]
        del self.freq_list_map[freq][key]  # Remove key from current frequency list

        if not self.freq_list_map[freq]:  # If no keys left at this frequency
            del self.freq_list_map[freq]
            if self.min_freq == freq:
                self.min_freq += 1  # Update min frequency

        # Move key to the next frequency level
        self.key_freq_map[key] += 1
        new_freq = self.key_freq_map[key]
        self.freq_list_map[new_freq][key] = None  # Add key to new frequency list

    def _evict_least_frequent(self):
        # Remove the least frequently used (LFU) key with lowest min_freq
        key, _ = self.freq_list_map[self.min_freq].popitem(last=False)  # Remove first (LRU) item
        del self.key_value_map[key]
        del self.key_freq_map[key]

