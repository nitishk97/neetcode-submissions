"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {} # stores original->cloned Node
        if not node:
            return None

        queue = deque([node]) # traverses the original graph
        cloned_node = Node(node.val)
        old_to_new[node] = cloned_node
        while queue:
            curr = queue.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in old_to_new:
                    cloned_neighbor = Node(neighbor.val)
                    old_to_new[neighbor] = cloned_neighbor
                    queue.append(neighbor)
                old_to_new[curr].neighbors.append(old_to_new[neighbor])  
        return old_to_new[node]               

        # # takes original node and returns cloned node
        # def dfs(node):
        #     if node in old_to_new:
        #         return old_to_new[node]
            
        #     cloned_node = Node(node.val)
        #     old_to_new[node] = cloned_node
        #     for neighbor in node.neighbors:
        #         cloned_node.neighbors.append(dfs(neighbor))
        #     return cloned_node
        # return dfs(node)