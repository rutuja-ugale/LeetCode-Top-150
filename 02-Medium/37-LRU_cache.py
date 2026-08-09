class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        """:type capacity: int"""
        self.capacity = capacity
        self.cache = {}  # key -> Node mapping
        
        # Dummy head and tail nodes
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        """Helper to remove a node from the doubly linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_head(self, node):
        """Helper to add a node right after the dummy head."""
        next_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next_node
        next_node.prev = node

    def get(self, key):
        """:type key: int
        :rtype: int"""
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_head(node)
            return node.val
        return -1

    def put(self, key, value):
        """:type key: int
        :type value: int
        :rtype: None"""
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add_to_head(node)
        else:
            if len(self.cache) >= self.capacity:
                # Evict the least recently used item (node before tail)
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]
            
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)