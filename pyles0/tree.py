tree_height = int(input('Enter the height of tree: '))

for i in range(1, tree_height * 2, 2):
    print(('*' * i).center(tree_height * 2))
