# Red-Black tree object implementation

class RedBlackTree:
    class TreeNode:
        def __init__(self, value, color='r', parent=None, left=None, right=None):
            self.value = value
            self.color = color
            self.parent = parent
            self.left = left
            self.right = right
            
        def inverse_color(self):
            # Change node color by inverting its current color
            self.color = 'b' if self.color == 'r' else 'r'
    
    # RedBlackTree Class
    def __init__(self):
        # Initialising tree properties
        self.nil = self.TreeNode(value=None, color='b')
        self.root = self.nil
        self._size = 0
    
    def search(self, word: str) -> bool:
        # Use balanced binary search method to find word node
        # takes O(log n) time
        x = self.root # start at root
        while x != self.nil: # while not at nil
            if x.value == word: # if word is found
                return True
            elif x.value < word: # if word is greater than current node
                x = x.right # go right
            else:
                x = x.left # go left
        return False # word not found
    
    def insert(self, word: str) -> bool:
        # Insert word into tree
        # does not allow duplicates
        # takes O(log n) time

        # Create tree node for word
        newNode = self.TreeNode(value=word)
        newNode.left = self.nil
        newNode.right = self.nil
        
        # Insert into tree as balanced binary search tree
        y = self.nil
        x = self.root
            # Traverse tree to find insertion point (parent of new node)
        while x != self.nil:
            y = x
            if newNode.value < x.value:
                x = x.left
            elif newNode.value > x.value:
                x = x.right
            else:
                # word already exists
                # add more safety to the function and does not allow duplicates
                print(f"Word '{word}' already exists in the tree.")
                return False
            # Set parent and insert node
        newNode.parent = y
        if y == self.nil:
            self.root = newNode
        elif newNode.value < y.value:
            y.left = newNode
        else:
            y.right = newNode
        
        # Fixup tree to maintain red-black properties
        self.__fixup(newNode)
        
        # Update properties
        self.__inc_tree_size()
        
        return True
            
    def tree_height(self):
        # Calculate height of tree
        # takes O(n) time
        return self.__get_node_height(self.root)

    def black_height(self):
        # Calculate black height of tree
        # takes O(log n) time
        x = self.root # starts at root
        black_height = 0
        while x != self.nil:
            if x.color == 'b':
                black_height += 1
            x = x.left # goes down left side of tree until nil
        return black_height
    
    def tree_size(self):
        return self._size
    
    def __left_rotate(self, x: TreeNode):
        y = x.right # y is x's right child
        x.right = y.left # x's right child becomes y's left child
        if y.left != self.nil:
            y.left.parent = x # y's left child's parent becomes x
        y.parent = x.parent # y's parent becomes x's parent
        if x.parent == self.nil:
            self.root = y # y becomes root
        elif x == x.parent.left:
            x.parent.left = y # y becomes x's parent's left child
        else:
            x.parent.right = y # y becomes x's parent's right child
        y.left = x # y's left child becomes x
        x.parent = y # x's parent becomes y
    
    def __right_rotate(self, x: TreeNode):
        y = x.left # y is x's left child
        x.left = y.right # x's left child becomes y's right child
        if y.right != self.nil:
            y.right.parent = x # y's right child's parent becomes x
        y.parent = x.parent # y's parent becomes x's parent
        if x.parent == self.nil:
            self.root = y # y becomes root
        elif x == x.parent.right:
            x.parent.right = y # y becomes x's parent's right child
        else:
            x.parent.left = y # y becomes x's parent's left child
        y.right = x # y's right child becomes x
        x.parent = y # x's parent becomes y
    
    def __fixup(self, z: TreeNode):
        while z.parent.color == 'r': # while z's parent is red
            if z.parent == z.parent.parent.left: # if z's parent is a left child
                y = z.parent.parent.right # y is z's parent's right child
                if y.color == 'r': # if y is red
                    z.parent.color = 'b' # z's parent becomes black
                    y.color = 'b' # y becomes black
                    z.parent.parent.color = 'r' # z's parent's parent becomes red
                    z = z.parent.parent # z becomes z's parent's parent
                else:
                    if z == z.parent.right: # if z is a right child
                        z = z.parent # z becomes z's parent
                        self.__left_rotate(z) # left rotate z
                    z.parent.color = 'b' # z's parent becomes black
                    z.parent.parent.color = 'r' # z's parent's parent becomes red
                    self.__right_rotate(z.parent.parent) # right rotate z's parent's parent
            else: # if z's parent is a right child
                y = z.parent.parent.left
                if y.color == 'r':
                    z.parent.color = 'b'
                    y.color = 'b'
                    z.parent.parent.color = 'r'
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.__right_rotate(z)
                    z.parent.color = 'b'
                    z.parent.parent.color = 'r'
                    self.__left_rotate(z.parent.parent)
        self.root.color = 'b'
    
    def __get_node_height(self, x: TreeNode):
        # Recursive helper function to calculate height of node
        if x == self.nil:
            return 0
        return 1 + max(self.__get_node_height(x.left), self.__get_node_height(x.right))
        
    def __inc_tree_size(self):
        self._size += 1