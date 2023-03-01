from linked_list2 import Node, LinkedList, Elemento, Search


# Nodes instantiation
node_a = Node('A')
node_b = Node('B')
node_c = Node('C')
node_d = Node('D')
node_e = Node('E')
node_f = Node('F')

# Node in memory
# print(node_a)
# print(id(node_a))

# Create LL
ll = LinkedList()
print(ll)

# Insert at beginning
ll.insert_at_beginning(node_c)
print(ll)
ll.insert_at_beginning(node_b)
print(ll)
ll.insert_at_beginning(node_a)
print(ll)
ll.insert_at_beginning(node_d)
print(ll)

# Insert at end
ll.insert_at_end(node_e)
print(ll)

# Insert before
ll.insert_before('A', node_f)
print(ll)

node_g = Node('G')
ll.insert_before('D', node_g)
print(ll)

node_h = Node('H')
ll.insert_before('E', node_h)
print(ll)

# Delete a given node
ll.delete('E')
print(ll)
ll.delete('D')
print(ll)
ll.delete('C')
print(ll)

#search


my_list = Search()
my_list.buscar(node_a)
valor = my_list.buscar ('A')
print(valor)
my_list.buscar(node_b)
valor = my_list.buscar ('B')
print(valor)
my_list.buscar(node_c)
valor = my_list.buscar ('C')
print(valor)
my_list.buscar(node_d)
valor = my_list.buscar ('D')
print(valor)
my_list.buscar(node_e)
valor = my_list.buscar ('E')
print(valor)
my_list.buscar(node_f)
valor = my_list.buscar ('F')

print(valor)