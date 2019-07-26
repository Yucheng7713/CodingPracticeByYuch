from functools import lru_cache
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def inorderSerialize(node):
            if not node: return ""
            return inorderSerialize(node.left) + str(node.val) + inorderSerialize(node.right)

        def preorderSerialize(node):
            if not node: return ""
            return str(node.val) + preorderSerialize(node.left) + preorderSerialize(node.right)

        s1 = s2 = root
        return inorderSerialize(s1) + '/' + preorderSerialize(s2)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def constructTree(inorderList, preorderList):
            if not inorderList:
                return None
            r_val = preorderList.pop(0)
            r_index = inorderList.index(r_val)
            root = TreeNode(r_val)
            root.left = constructTree(inorderList[:r_index], preorderList)
            root.right = constructTree(inorderList[r_index + 1:], preorderList)
            return root

        inorder, preorder = tuple(data.split('/'))
        return constructTree([int(s) for s in inorder], [int(s) for s in preorder])

# Use preorder DFS method - not quite efficient
class Codec_II:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        result = []
        def preorderDFS(node, result):
            if not node:
                result += ['#']
                return
            result += [str(node.val)]
            preorderDFS(node.left, result)
            preorderDFS(node.right, result)

        preorderDFS(root, result)
        return " ".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        serial_tree = data.split(' ')

        def constructTree():
            r_val = serial_tree.pop(0)
            if r_val == '#':
                return None
            node = TreeNode(int(r_val))
            node.left = constructTree()
            node.right = constructTree()
            return node

        return constructTree()
a, b, c, d, e = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5)
a.left, a.right = b, c
c.left, c.right = d, e
print(Codec_II().serialize(a))
# data = "1,2, , ,3,4, , ,5, , "
# print(Codec_II().deserialize(data))

