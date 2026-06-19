class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} 
        
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def _remove(self, node):
        prev_node, next_node = node.prev, node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _insert(self, node):
        prev_node, next_node = self.right.prev, self.right
        prev_node.next = node
        next_node.prev = node
        node.prev = prev_node
        node.next = next_node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert(node) 
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
            
        new_node = Node(key, value)
        self.cache[key] = new_node
        self._insert(new_node)
        
        if len(self.cache) > self.capacity:
            lru_node = self.left.next
            self._remove(lru_node)
            del self.cache[lru_node.key]