nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
result = [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]
from dataclasses import dataclass

@dataclass
class Node():
    val: int
    left: Node
    right: Node

def make_binary_tree(nodeinfo: list[int, int, int]) -> Node:

    if len(nodeinfo) == 1:
        return Node(nodeinfo[0][2], None, None)

    if len(nodeinfo) == 0:
        return None

    sorted_nodeinfo = sorted(nodeinfo, key=lambda i: i[1], reverse=True)
    parent_x = sorted_nodeinfo[0][0]
    parent_val = sorted_nodeinfo[0][2]

    left = list(filter(lambda i: i[0] < parent_x, sorted_nodeinfo))
    right = list(filter(lambda i: i[0] > parent_x, sorted_nodeinfo))

    return Node(parent_val, left=make_binary_tree(left), right=make_binary_tree(right))

def preorder(node: Node) -> None:
    if node is None:
        return []
    return [node.val] + preorder(node.left) + preorder(node.right)
    

def postorder(node: Node) -> None:
    if node is None:
        return []
    
    if node.left is None and node.right is None:
            return [node.val]
    return postorder(node.left) + postorder(node.right) + [node.val]
    

if __name__=="__main__":
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)

    print(make_binary_tree(nodeinfo))
    bt = make_binary_tree(nodeinfo)
    print(preorder(bt))
    print(postorder(bt))

    
    
    

        


