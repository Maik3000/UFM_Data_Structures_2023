from bst import BinarySearchTree

# Instantiate BST
print('\n*** Instantiate BST ***\n')
bst = BinarySearchTree()
print('BST object: {}'.format(bst)) # bst object
print('Current root: {}'.format(bst.root)) # empty root


# Inserts
print('\n*** Inserting Nodes in Tree ***\n')
# n = 10
nodes_values = [33, 77, 4, 11, 16, 55, 5, 1, 14, 63]

# for _ in range(n):
#     nodes_values.append(random.randint(0, 100))

for value in nodes_values:
    print('Inserting node with value: {}'.format(value))
    bst.insert(value)

print('Current root: {}'.format(bst.root)) # current root


# Traverse
print('\n*** Traversing Tree ***\n')
bst.traverse(bst.root)


# Search 
print('\n*** Searching keys in Tree ***\n')
test_keys = [33, 44, 2, 3, 4, 63, 1]

for key in test_keys:
    print('Searching for {}: {}'.format(key, bst.search(key)))


# Min-Max 
print('\n*** Searching for min-max in Tree ***\n')
print('Min: {}'.format(bst.find_min(bst.root)))
print('Max: {}'.format(bst.find_max(bst.root)))

# Delete
print('\n*** Delete in Tree ***\n')
print("Tree original")
print(bst.print_tree("tree")) 

bst.delete(11)
bst.delete(55)
bst.delete(4)

print("\nTree with deletes: \n" + bst.print_tree("tree"))


