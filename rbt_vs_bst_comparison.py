# Ahmed Abd Al Moneim
# Details: 
#       ID: 9284
#       Group: 3
#       Section: 1
#Benchmark cmpring RBT vs BST in terms of insertion&search speed and height.
import time
import random
from red_black_tree import RedBlackTree

class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left=None
        self.right=None
# normal bst code just for comparing
class BST:
    def __init__(self):
        self.root = None
    def insert(self,key):
        if not self.root:
            self.root=BSTNode(key)
            return
        cur=self.root
        while True:
            if key<cur.key:
                if cur.left:
                    cur=cur.left
                else:
                    cur.left=BSTNode(key)
                    return
            elif key>cur.key:
                if cur.right:
                    cur=cur.right
                else:
                    cur.right=BSTNode(key)
                    return
            else:
                return
    def search(self, key):
        cur = self.root
        while cur:
            if key == cur.key:
                return True
            cur = cur.left if key < cur.key else cur.right
        return False
    def height(self, node):
      if node is None:
        return 0
      return 1 + max(self.height(node.left), self.height(node.right))

#samples for testing
def run_test(n=5000):
    data = list(range(n))
    random.shuffle(data)
    print(f"\nRunning test with {n} elements\n")

    #red black trees
    rbt = RedBlackTree()
    start = time.time()
    for x in data:
        rbt.insert(str(x))
    rbt_insert = time.time() - start
    start = time.time()
    for x in data[:1000]:
        rbt.search(str(x))
    rbt_search = time.time() - start

    #bst
    bst = BST()
    start = time.time()
    for x in data:
        bst.insert(x)
    bst_insert = time.time() - start
    start = time.time()
    for x in data[:1000]:
        bst.search(x)
    bst_search = time.time() - start

    #resluts comparison
    print("Red-Black Tree:")
    print(" Insert time:",round(rbt_insert,4))
    print(" Search time:",round(rbt_search,4))
    print(" Height:", rbt.tree_height())
    print("\nBST:")
    print(" Insert time:", round(bst_insert,4))
    print(" Search time:",round(bst_search,4))
    print("Height:",bst.height(bst.root))

if __name__ == "__main__":
    run_test()
