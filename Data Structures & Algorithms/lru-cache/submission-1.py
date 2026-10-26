class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node

        # dummy nodes
        self.left = Node()   # LRU side
        self.right = Node()  # MRU side

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        """Remove node from linked list."""
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        """Insert node at MRU end."""
        prev = self.right.prev

        prev.next = node
        node.prev = prev

        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # accessing it makes it most recently used
        self.remove(node)
        self.insert(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]

            # update value
            node.val = value

            # move to MRU
            self.remove(node)
            self.insert(node)

        else:
            node = Node(key, value)
            self.cache[key] = node
            self.insert(node)

        # over capacity -> remove LRU
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
