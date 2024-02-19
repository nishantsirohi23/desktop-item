def dfs_recursive(graph, current_node, visited):
    visited.add(current_node)

    for neighbor in graph.get(current_node, []):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

def find_reachable_nodes_recursive(graph, start_node):
    visited = set()
    dfs_recursive(graph, start_node, visited)
    return visited
def nodes_to_block(graph, start_node, target_node):
    reachable_nodes_from_start = find_reachable_nodes_recursive(graph, start_node)

    nodes_to_block_list = []
    for node in reachable_nodes_from_start:
        if target_node in graph.get(node, []):
            nodes_to_block_list.append(node)

    return nodes_to_block_list

# Given data
edges = [(2, 9), (7, 2), (7, 9), (9, 5)]
mylist = {2: [9], 5: [], 7: [2, 9], 9: [5]}

# Specify the nodes to block (2 cannot reach 5)
start_node_to_block = 2
target_node_to_block = 5

# Find the list of members to be blocked
members_to_block = nodes_to_block(mylist, start_node_to_block, target_node_to_block)

# Print the list of members to be blocked
print("Members to be blocked:", members_to_block)
