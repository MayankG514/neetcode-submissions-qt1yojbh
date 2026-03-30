class LRUCache:

    class Node:
        def __init__(self,key,val):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None
    
    def addNode(self,newNode: Node):
        temp = self.head.next
        self.head.next = newNode
        newNode.next = temp
        newNode.prev = self.head
        temp.prev = newNode
    
    def delNode(self,delNode: Node):
        prevv = delNode.prev
        nextt = delNode.next
        prevv.next = nextt
        nextt.prev = prevv

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hm = {}
        self.head = self.Node(-1,-1)
        self.tail = self.Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head        

    def get(self, key: int) -> int:
        if key in self.hm:
            n = self.hm[key]
            ans = n.val
            del self.hm[key]
            self.delNode(n)
            self.addNode(n)
            self.hm[key] = self.head.next
            return ans
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            n = self.hm[key]
            del self.hm[key]
            self.delNode(n)

        if len(self.hm) == self.cap:
            t = self.tail.prev
            self.delNode(t)
            del self.hm[t.key]
        
        newNode = self.Node(key,value)
        self.addNode(newNode)
        self.hm[key] = self.head.next
        



        
