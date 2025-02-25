class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.pairs = {}
        self.head = ListNode(-1,-1)
        self.tail = ListNode(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def get(self, key: int) -> int:
        if key not in self.pairs: 
            return -1

        node = self.pairs[key]
        self.remove(node)
        self.insert(node)

        return node.value
    
    def put(self, key: int, value: int) -> None:
        if key in self.pairs:
            old_node = self.pairs[key]
            self.remove(old_node)
        
        new_node = ListNode(key,value)
        self.pairs[key] = new_node
        self.insert(new_node)

        if len(self.pairs) > self.cap:
            lru_node = self.head.next
            self.remove(lru_node)
            del self.pairs[lru_node.key]
        
    def insert(self, node):
        curr_tail = self.tail.prev
        curr_tail.next= node
        node.prev = curr_tail
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


        

        


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)