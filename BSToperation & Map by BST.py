# BST operation & Map by BST
# 2018015027 김한탁
# 이진탐색 트리의 연산과 이진탐색트리를 이용한 맵 클래스

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
    
def delete_bst_case1(parent, node, root):
    if parent is None:
        root = None
    else:
        if parent.left == node:
            parent.left = None
        else:
            parent.right = None

    return root

def delete_bst_case2(parent, node, root):
    if node.left is None:
        child = node.right
    else:
        child = node.left

    if node == root:
        root = child
    else:
        if node is parent.left:
            parent.left = child
        else:
            parent.right = child

        return root

def delete_bst_case3(node, root):
    succp = node
    succ = node.right
    while succ.left is not None:
        succp = succ  # one step donw
        succ = succ.left  # succeed to left

    if succp.left is succ:
        succp.left = succ.right
    else:
        succp.right = succ.right

    node.key = succ.key
    node.value = succ.value
    node = succ

    return root

def delete_bst(root, key):
    if root is None:
        return None

    parent = None
    node = root
    while node is not None and node.key is not key:
        parent = node
        if key < node.key:
            node = node.left
        else:
            node = node.right

    if node is None:
        return None
    if node.left is None and node.right is None:
        root = delete_bst_case1(parent, node, root)
    elif node.left is None or node.right is None:
        root = delete_bst_case2(parent, node, root)
    else:
        root = delete_bst_case3(node, root)
    return root

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

    def delete(self, key):
        return delete_bst(self.root, key)

    def display(self, msg = "BSTMap : "):
        print(msg, end='')
        inorder(self.root)
        print()

def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.key, end=' ')
        inorder(n.right)

def count_node(n):
    if n is None:
        return 0
    else:
        return 1+count_node(n.left) + count_node(n.right)    
    
map=BSTMap()
data=[35, 18, 7, 26, 12, 3, 68, 22, 30, 99]

print("[삽입연산]: ", data)
for key in data:
    map.insert(key)
map.display("[중위 순회]: ")
if map.search(26) != None : print("[탐색 26] :  성공")
else: print("[탐색 26] : 성공")
if map.search(25) != None : print("[탐색 25 ] : 성공")
else: print("[탐색 25] : 실패")

map.delete(3); map.display("[   3 삭제]: ")
map.delete(68); map.display("[  18 삭제]: ")
map.delete(18); map.display("[  68 삭제]: ")
map.delete(35); map.display("[  35 삭제]: ")