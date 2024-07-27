# AVL Tree operation & Map by AVL 
# 2018015027 김한탁
# AVL BST의 연산 및 AVL트리를 이용한 맵

from CircularQueue import *

def rotateLL(A):
    B = A.left
    A.left = B.right
    B.right = A
    return B

def rotateRR(A):
    B = A.right
    A.right = B.left
    B.left = A
    return B

def rotateRL(A):
    B = A.right
    A.right = rotateLL(B)
    return rotateRR(A)

def rotateLR(A):
    B = A.left
    A.left = rotateRR(B)
    return rotateLL(A)

def reBalance(parent):
    hDiff = calc_height_diff(parent)

    if hDiff > 1:
        if calc_height_diff(parent.left) > 0:
            parent = rotateLL(parent)
        else:
            parent = rotateLR(parent)
    elif hDiff < -1:
        if calc_height_diff(parent.right) < 0:
            parent = rotateRR(parent)
        else:
            parent = rotateRL(parent)
    return parent

def calc_height(n):
    if n is None:
        return 0
    hleft = calc_height(n.left)
    hright = calc_height(n.right)
    if hleft > hright:
        return hleft + 1
    else:
        return hright + 1

def calc_height_diff(n):
    left = calc_height(n.left)
    right = calc_height(n.right)
    return left - right

def insert_avl(parent, node):
    if node.key < parent.key:
        if parent.left is not None:
            parent.left = insert_avl(parent.left, node)
        else:
            parent.left = node
        return reBalance(parent)
    elif node.key > parent.key:
        if parent.right is not None:
            parent.right = insert_avl(parent.right, node)
        else:
            parent.right = node
        return reBalance(parent)
    else:
        print("중복된 키 에러")



class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

def search_bst(n, key):
    if n == None:
        return None
    elif key == n.key:
        return search_bst(n.left, key)
    else:
        return search_bst(n.right, key)

def search_value_bst(n, value):
    if n == None:
        return None
    elif value == n.value:
        return n
    res = search_value_bst(n.left, value)
    
    if res is not None:
        return res
    else:
        return search_value_bst(n.right, value)

def search_bst_iter(n, key):
    while n!=None:
        if key == n.key:
            return n
        elif key < n.key:
            n = n.left
        else:
            n = n.right
    return None

def search_max_bst(n):
    while n != None and n.right != None:
        n = n.right
    return n

def search_min_bst(n):
    while n != None and n.left != None:
        n = n.left
    return n

def insert_bst(r, n):
    if n.key < r.key:
        if r.left is None:
            r.left = n
            return True
        else:
            return insert_bst(r.left, n)
    elif n.key > r.key:
        if r.right is None:
            r.right = n
            return True
        else:
            return insert_bst(r.right, n)
    else:
        return False
    

class BSTMap():
    def __init__(self):
        self.root = None 

    def isEmpty(self):
        return self.root is None

    def clear(self):
        self.root = None

    def size(self):
        return count_node(self.root)

    def search(self, key):
        return search_bst( self.root, key)

    def searchValue(self, key):
        return search_value_bst(self.root, key)

    def findmax(self):
        return search_max_bst(self, self.root)

    def findmin(self):
        return search_min_bst(self.root)

    def insert(self, key, value=None):
        n = BSTNode(key, value)
        if self.isEmpty():
            self.root = n
        else:
            insert_bst(self.root, n)



class AVLMap(BSTMap):
    def __init__(self):
        super().__init__()
        
    def isEmpty(self):
        return self.root is None    

    def insert(self, key, value=None):
        n = BSTNode(key, value)
        if self.isEmpty():
            self.root = n
        else:
            self.root = insert_avl(self.root, n)

    def display(self, msg = "BSTMap : "):
        print(msg, end=' ')
        levelorder(self.root)
        print()
            
def levelorder(root):
    queue = CircularQueue()
    queue.enqueue(root)
    while not queue.isEmpty() :
        n = queue.dequeue()
        if n is not None:
            print(n.key, end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)
            
def count_node(n):
    if n is None:
        return 0
    else:
        return 1+count_node(n.left) + count_node(n.right)    

def count_leaf(n):
    if n is None:
        return 0
    elif n.left is None and n.right is None:
        return 1
    else:
        return count_leaf(n.left) + count_leaf(n.right)


node = [7, 8, 9, 2, 1, 5, 3, 6, 4]
map=AVLMap()

for i in node:
    map.insert(i)
    map.display("AVL(%d): " %i)
      
print("노드의 개수 = %d" % count_node(map.root)) 
print("단말의 개수 = %d" % count_leaf(map.root)) 
print("트리의 높이 = %d" % calc_height(map.root))    
    