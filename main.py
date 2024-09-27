class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Node) -> Node:
        if not node:
            return None
        
        # Dictionary to keep track of cloned nodes
        clone_map = {}

        # Define a recursive DFS function to clone the graph
        def dfs(original):
            if original in clone_map:
                return clone_map[original]
            
            # Clone the node
            clone_node = Node(original.val)
            clone_map[original] = clone_node
            
            # Clone neighbors
            for neighbor in original.neighbors:
                clone_node.neighbors.append(dfs(neighbor))
                
            return clone_node
        
        # Start the DFS from the given node
        return dfs(node)

# Example usage:
# Assuming we have a graph constructed using Node class
# To test, you can create a graph and call cloneGraph on the starting node.

# Example Graph Construction
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

solution = Solution()
cloned_graph = solution.cloneGraph(node1)

# Function to print the graph for verification
def print_graph(node):
    visited = set()
    def dfs(n):
        if n in visited:
            return
        visited.add(n)
        print(n.val, [neighbor.val for neighbor in n.neighbors])
        for neighbor in n.neighbors:
            dfs(neighbor)
    
    dfs(node)

print("Original graph:")
print_graph(node1)

print("\nCloned graph:")
print_graph(cloned_graph)
