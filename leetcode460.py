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

from collections import defaultdict

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1  # Frequency starts at 1 upon insertion
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(-1, -1)  # Dummy head
        self.tail = Node(-1, -1)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_to_front(self, node):
        # Insert node right after head
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def remove(self, node):
        # Remove the node from the list
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None
        return node

    def remove_last(self):
        # Remove the least recently used node (before tail)
        if self.is_empty():
            return None
        return self.remove(self.tail.prev)

    def is_empty(self):
        return self.head.next == self.tail

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0
        self.key_node_map = {}  # Maps key to node
        self.freq_list_map = defaultdict(DoublyLinkedList)  # Maps frequency to DoublyLinkedList

    def get(self, key: int) -> int:
        if key not in self.key_node_map or self.capacity == 0:
            return -1
        
        node = self.key_node_map[key]
        self._update_frequency(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        if key in self.key_node_map:
            # Update existing node's value and frequency
            node = self.key_node_map[key]
            node.value = value
            self._update_frequency(node)
        else:
            if self.size == self.capacity:
                # Evict the least frequently used (and least recently used) node
                lfu_list = self.freq_list_map[self.min_freq]
                node_to_remove = lfu_list.remove_last()
                if node_to_remove:
                    del self.key_node_map[node_to_remove.key]
                    self.size -= 1

            # Insert new node
            new_node = Node(key, value)
            self.key_node_map[key] = new_node
            self.freq_list_map[1].add_to_front(new_node)
            self.min_freq = 1
            self.size += 1

    def _update_frequency(self, node):
        freq = node.freq
        self.freq_list_map[freq].remove(node)

        if self.freq_list_map[freq].is_empty():
            del self.freq_list_map[freq]
            if self.min_freq == freq:
                self.min_freq += 1

        # Increment frequency and move to new frequency list
        node.freq += 1
        self.freq_list_map[node.freq].add_to_front(node)
