# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Construct binary tree from preorder and inorder sequence lists
# This approach only works for binary search tree but for binary tree
class Codec_I:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def inorderSerialize(node):
            if not node: return []
            return inorderSerialize(node.left) + [str(node.val)] + inorderSerialize(node.right)

        def preorderSerialize(node):
            if not node: return []
            return [str(node.val)] + preorderSerialize(node.left) + preorderSerialize(node.right)

        if not root: return ""
        s1 = s2 = root
        return ",".join(inorderSerialize(s1)) + '/' + ",".join(preorderSerialize(s2))

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

        if not data: return None
        inorder, preorder = tuple(data.split('/'))
        return constructTree(list(map(int, inorder.split(','))), list(map(int, preorder.split(','))))


t1, t2, t3, t4, t5, t6, t7 = TreeNode(5), TreeNode(3), TreeNode(7), TreeNode(2), TreeNode(4), TreeNode(6), TreeNode(9)
t1.left, t1.right = t2, t3
t2.left, t2.right = t4, t5
t3.left, t3.right = t6, t7
# codec = Codec()
# t_str = codec.serialize(t1)
t_str = "5 3 2 4 7 6 9"
r_str = "5324769"
print(list(map(int, t_str.split())))
print([int(ch) for ch in r_str])
