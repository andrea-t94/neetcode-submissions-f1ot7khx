class Node:
    def __init__(self, key, val):
        # is is necessary to point to hMap
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    ''' doubly linked list makes add/remove a node in O(1) since hMap points to the node
    with an array I would have done linear search '''
    def __init__(self, capacity: int):
        self.cache = {} #key: node
        self.cap = capacity
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        
    def remove(self, node):
        ''' removal is O(1), prev points to next '''
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    
    def insert(self, node):
        ''' insertion is O(1), node points at right '''
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt
        
    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key]) #in O(1) we access the node!
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # drop the node to the left most (least used)
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        
