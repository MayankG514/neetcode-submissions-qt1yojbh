class LRUCache:

    class Node:
        def __init__(self,key,val):
            self.key = key
            self.val = val
            self.next = None
            self.prev = None

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = self.Node(-1,-1)
        self.tail = self.Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hm = {}
    
    def addNode(self, newNode):
        t = self.head.next
        self.head.next = newNode
        newNode.prev = self.head
        newNode.next = t
        t.prev = newNode
    
    def delNode(self, node):
        prevv = node.prev
        nextt = node.next
        prevv.next = nextt
        nextt.prev = prevv

    def get(self, key: int) -> int:
        if key in self.hm:
            node = self.hm[key]
            ans = node.val
            del self.hm[key]
            self.delNode(node)

            self.addNode(node)
            self.hm[key] = self.head.next
            return ans
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            n = self.hm[key]
            self.delNode(n)
            del self.hm[key]
        
        if len(self.hm) == self.cap:
            n = self.tail.prev
            del self.hm[n.key]
            self.delNode(n)
        
        newNode = self.Node(key,value)
        self.addNode(newNode)
        self.hm[key] = self.head.next


        
