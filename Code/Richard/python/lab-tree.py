import random
import pprint
# build a 'tree' using a recursive function

names = ['virginia', 'christine', 'carl', 'lillian']


def generate_tree(depth):
    n_children = int(random.random()*10/depth)
    if n_children == 0:
        return {'type': 'leaf', 'name': random.choice(names)}
    branch = {'type': 'branch', 'children': []}
    for i in range(n_children):
        child = generate_tree(depth+1)
        branch['children'].append(child)
    print(branch)
    return branch

# print the tree. To see the tree as a collection of dicts, uncomment the 'print branch' line above.

def print_node(node, indentation):
    if node['type'] == 'leaf':
        print(indentation + node['name'])
    else:
        print(indentation + '-')
        for i in range(len(node['children'])):
            print_node(node['children'][i], indentation + '\t')


# count all trees and branches

def count_nodes(node):
    if node['type'] == 'leaf':
        return 1
    r = 1
    for i in range(len(node['children'])):
        r += count_nodes(node['children'][i])
    return r

# count the leaves. Loop through children, calling the function recursively

def count_leaves(node):
    if node['type'] == 'leaf':
        return 1
    count = 0
    for i in range(len(node['children'])):
        count += count_leaves(node['children'][i])
    return count

# rename a leaf

def rename_leaf(node, orig, replace):
    if node['type'] == 'leaf':
        if node['name'] == orig:
            node['name'] = replace
    else:
        for i in range(len(node['children'])):
            rename_leaf(node['children'][i], orig, replace)


root = generate_tree(1)
print_node(root, '')
print(f'The number of nodes is {count_nodes(root)}.')
print(f'The number of leaves is {count_leaves(root)}.')

rename_leaf(root, 'carl', 'abcxyzdefghijkl')
print_node(root, '')