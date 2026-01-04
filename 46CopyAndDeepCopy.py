from copy import copy , deepcopy
#shallow Copy
'''
l1 = [1, 2, [10, 20, 30], 4, 5, 6]

l2 = copy(l1)
l2[2].append(99)

print(l1)
print(l2)

'''
#deepcopy
'''
from copy import deepcopy

l1 = [1, 2, [10, 20, 30], 4, 5, 6]
l2 = deepcopy(l1)
l2[2].append(99)

print(l1)
print(l2)

'''






















