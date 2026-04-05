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
        self._black_height = 0
        self._height = 0
    
    def search(self, word: str) -> bool:
        # Use balanced binary search method to find word node
        return False
    
    def insert(self, word: str) -> None:
        # Create tree node for word
        
        # Insert into tree as balanced binary search tree
        
        # Fixup
        
        # Update properties
        self.__inc_tree_size()
            
    def tree_height(self):
        return self._height
    
    def black_height(self):
        return self._black_height
    
    def tree_size(self):
        return self._size
    
    def __left_rotate(self, x: TreeNode):
        # Left rotate
        pass
    
    def __right_rotate(self, x: TreeNode):
        # Right rotate
        pass
    
    def __fixup(self, z: TreeNode):
        # Fixup red-black tree
        pass
        
    def __inc_tree_size(self):
        self._size += 1