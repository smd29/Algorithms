class node:
    def __init__(self,freq,chars,left=None,right=None):
        self.freq = freq
        self.chars = chars
        self.left = left
        self.right = right
        self.huff = '' #0/1 tree

def printing(node, val=''):
    newVal = val + str(node.huff)
    if(node.left):
        printing(node.left,newVal)
    if(node.right):
        printing(node.right,newVal)
    if(not node.left and not node.right):
        print(f"{node.chars} --> {newVal}")

#driver code
chars = ['a', 'b', 'c', 'd']
freq = [50,40,5,5]
nodes = []

for x in range(len(chars)):
    nodes.append(node(freq[x], chars[x]))

while len(nodes)>1:
    nodes = sorted(nodes, key=lambda x: x.freq)

    left = nodes[0]
    right = nodes[1]

    left.huff = 0
    right.huff = 1

    newNode = node(left.freq+right.freq, left.chars+right.chars, left, right)
    nodes.remove(left)
    nodes.remove(right)
    nodes.append(newNode)

printing(nodes[0])
print("Time Complexity: O(n**2*log n)")
