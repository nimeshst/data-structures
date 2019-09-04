# Tree datastructure can be represented using list or 
# in this case OOP paradigm . We define a class that has 
# attributes for root as well as right and left subtree


class TreeNode:
    """
    contains the node data structure with attributes left
    and right 
    """
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.right = right
        self.left = left
    
    def __repr__(self):
        return repr(self.data)
    
    def get_data(self):
        return self.data
    
    def set_data(self, data):
        self.data = data
    
    def get_right(self):
        return self.right
    
    def get_left(self):
        return self.left
    
    def set_left(self, node):
        self.left = node
    
    def set_right(self, node):
        self.right = node

class BinaryTree:
    
    
    def __init__(self):
        self.root = None
    
    def insert(self,data):
        """
        insert the data at the binary tree
        """
        if self.root is None:
            # create the root node
            self.root = TreeNode(data = data)
        else :
            # compare the data with node data
            # to check where the node should be 
            # placed
            current = self.root
            parent = None
            while True:
                parent = current
                # go to the left
                if data < parent.get_data():
                    current = current.get_left()
                    if current == None:
                        # node insertion at left
                        parent.set_left(TreeNode(data = data))
                        return
                # go to the right
                else:
                    current = current.get_right()
                    if(current == None):
                        # node insertion
                        parent.set_right(TreeNode(data = data))
                        return

    def search(self , data):
        if self.root == data:
            return self.root
        else:
            current = self.root
            
            while current.get_data() != data:
                if current != None:
                    print(current.get_data())
                if data > current.get_data():
                    # go to the right subtree
                    current = current.get_right()
                else :
                    current = current.get_left()
                # not found
                if current == None:
                    return None

            return current.get_data()
   

def inorder(root):
    """
    Traverse the left subtree
    visit the root 
    Traverse the right subtree
    """
    if root:
        inorder(root.get_left())
        print(root.get_data())
        inorder(root.get_right())

def postorder(root):
    """
    Traverse the left subtree
    Traverse the right subtree
    visit the root 
    """
    if root:
        # first recur on left
        postorder(root.get_left())
        # recur on right
        postorder(root.get_right())
        print(root.get_data())

def preorder(root):
    """
    Traverse the root
    Traverse the left subtree
    Traverse the right subtree
    """
    if root:
        print(root.get_data())
        # recur on left child
        preorder(root.get_left())
        #recur on right child
        preorder(root.get_right())



