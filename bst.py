# Binary Tree
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Tree:
    def RECURinsertIntoBST(self, root: Node, val:int) -> Node:
        if not root:
            return Node(val)
        if val > root.val:
            root.right = self.RECURinsertIntoBST(root.right, val)
        elif val < root.val:
            root.left = self.RECURinsertIntoBST(root.left, val)
        return root

    def RECURdeleteNode(self, root:Node, key: int) -> Node:
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else: # delete root
            # No children
            if not root.left and not root.right:
                return None 
            
            # One Child
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            # Two children
            else:
                # search for minimum val in right tree
                curr = root
                while curr.left:
                    curr = curr.left
                root.val = curr.val
                root.right = self.RECURdeleteNode(root.right, curr.val)

        return root

    def dfs(self, root, mode):
        tr = []
        
        def inOrder(root):
            if not root:
                return
            inOrder(root.left)
            tr.append(root.val)
            inOrder(root.right)

        def preOrder(root):
            if not root:
                return
            tr.append(root.val)
            inOrder(root.left)
            inOrder(root.right)

        def postOrder(root):
            if not root:
                return
            inOrder(root.left)
            inOrder(root.right)
            tr.append(root.val)
        
        if mode == "in":
            inOrder(root)
        elif mode == "pre":
            preOrder(root)
        else:
            postOrder(root)
        return tr



    def ITERinsertIntoBST(self, root: Node, val: int) -> Node:
        if not root:
            return Node(val)
        curr = root
        while True:
            if curr.val == val:
                return root
            if curr.val > val:
                if not curr.left:
                    curr.left = Node(val)
                    return root
                curr = curr.left
            elif curr.val < val:
                if not curr.right:
                    curr.right = Node(val)
                    return root
                curr = curr.right
    
    def ITERdeleteNode(self, root: Node, key: int) -> Node:
        if not root:
            return None
        parent = None
        curr = root
        while curr:
            if curr.val == key:
                # Case 1: Node to be deleted has no children or only one child
                if not curr.left or not curr.right:
                    if not parent:  # If root needs to be deleted
                        return curr.left or curr.right
                    if parent.left == curr:
                        parent.left = curr.left or curr.right
                    else:
                        parent.right = curr.left or curr.right
                    return root
                
                # Case 2: Node to be deleted has two children
                successor_parent = curr
                successor = curr.right
                while successor.left:
                    successor_parent = successor
                    successor = successor.left
                curr.val = successor.val
                # Now delete successor which is either a leaf node or has right child only
                if successor_parent.left == successor:
                    successor_parent.left = successor.right
                else:
                    successor_parent.right = successor.right
                return root
                
            elif curr.val > key:
                parent = curr
                curr = curr.left
            else:
                parent = curr
                curr = curr.right
        
        return root

def print_tree(root, level=0, prefix="Root: ", max_depth=None):
    if root is None:
        return
    if max_depth is not None and level >= max_depth:
        return

    print(" " * (level * 4) + prefix + str(root.val))

    print_tree(root.left, level + 1, "L-- ", max_depth)
    print_tree(root.right, level + 1, "R-- ", max_depth)


root = Node(val=10)
root.left = Node(val=5)
root.right = Node(val=15)
m = Tree()
m.ITERinsertIntoBST(root, 12)
m.ITERinsertIntoBST(root, 1)
m.ITERinsertIntoBST(root, 23)
m.RECURinsertIntoBST(root, 39)
m.RECURinsertIntoBST(root, 21)
m.RECURinsertIntoBST(root, 29)
print(m.dfs(root, "in"))
print_tree(root)
m.ITERdeleteNode(root, 1)
print_tree(root)
