class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        # Dummy head and tail nodes
        self.first = ListNode(0, 0)
        self.last = ListNode(0, 0)
        self.first.right = self.last
        self.last.left = self.first

    # HELPER 1: Completely detach a node from its current neighbors
    def _remove(self, node: ListNode):
        prev_node = node.left
        next_node = node.right
        prev_node.right = next_node
        next_node.left = prev_node

    # HELPER 2: Always place a node right after the dummy 'first' head
    def _insert_at_head(self, node: ListNode):
        second = self.first.right
        self.first.right = node
        node.left = self.first
        node.right = second
        second.left = node

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self._remove(node)         # Remove from middle
            self._insert_at_head(node) # Move to front (Most Recently Used)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            # Key exists: update its value and move to front
            node = self.map[key]
            node.val = value
            self._remove(node)
            self._insert_at_head(node)
        else:
            # If cache is at full capacity, evict the LRU item
            if len(self.map) == self.capacity:
                lru_node = self.last.left
                self._remove(lru_node)
                del self.map[lru_node.key] # FIX 1: Explicitly delete from map!
            
            # Create and add the new node
            new_node = ListNode(key, value)
            self.map[key] = new_node
            self._insert_at_head(new_node)
