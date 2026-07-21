# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        from collections import deque
        if not root:
            return ""
        q = deque([root])
        arr = [str(root.val)]

        while q:
            node = q.popleft()       
            if node.left:
                arr.append(str(node.left.val))
                q.append(node.left)
            else:
                arr.append("N")
            if node.right:
                arr.append(str(node.right.val))
                q.append(node.right)
            else:
                arr.append("N")
        
        return ",".join(arr)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        from collections import deque
        if not data:
            return None
        vals = data.split(",")
        root = TreeNode(int(vals[0]))
        i = 1
        q = deque([root])

        while q:
            node = q.popleft()
            
            if vals[i] != "N":
                node.left = TreeNode(int(vals[i]))
                q.append(node.left)
            i+=1

            if vals[i] != "N":
                node.right = TreeNode(int(vals[i]))
                q.append(node.right)
            i+=1
        return root

