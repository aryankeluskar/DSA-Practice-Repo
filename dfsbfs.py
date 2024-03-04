import queue
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Tree:
    def bfs(self, root) -> list:
        if not root:
            return []
        tr = queue.Queue()
        tr.put(root)
        final = []
        while not tr.empty():
              curr = tr.get()
              final.append(curr.val)
              if curr.left:
                  tr.put(curr.left)
              if curr.right:
                  tr.put(curr.right)

            #   tr.get()

        return final

    def dfs(self, head, mode) -> list:
            tr = []
            root = head
            
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
    
    def RECURinsertIntoBST(self, root: Node, val:int) -> Node:
        if not root:
            return Node(val)
        if val > root.val:
            root.right = self.RECURinsertIntoBST(root.right, val)
        elif val < root.val:
            root.left = self.RECURinsertIntoBST(root.left, val)
        return root
    
root = Node(val=10)
root.left = Node(val=5)
root.right = Node(val=15)
m = Tree()
m.RECURinsertIntoBST(root, 12)
m.RECURinsertIntoBST(root, 1)
m.RECURinsertIntoBST(root, 23)
m.RECURinsertIntoBST(root, 39)
m.RECURinsertIntoBST(root, 21)
m.RECURinsertIntoBST(root, 29)
print(m.dfs(root, "in"))
print(m.bfs(root))