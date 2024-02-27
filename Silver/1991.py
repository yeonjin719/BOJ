N = int(input())
tree = [0]*N
for i in range(N):
    parent, leftC, rightC = input().split()
    tree[ord(parent)-65] = [leftC, rightC]

def preorder_traverse(node, visited):
    visited[ord(node)-65] = True
    print(node, end='')
    for i in tree[ord(node)-65]:
        if i != '.' and not visited[ord(i)-65]:
            preorder_traverse(i, visited)

def inorder_traverse(node, visited):
    if tree[ord(node)-65][0] != '.' and not visited[ord(tree[ord(node)-65][0])-65]:
        inorder_traverse(tree[ord(node)-65][0], visited)
        print(node, end='')
        visited[ord(node)-65] = True

        if tree[ord(node)-65][1] != '.' and not visited[ord(tree[ord(node)-65][1])-65]:
            inorder_traverse(tree[ord(node)-65][1], visited)
            visited[ord(tree[ord(node)-65][1])-65] = True

    elif tree[ord(node)-65][0] == '.' and not visited[ord(node)-65]:
        print(node, end='')
        visited[ord(node)-65] = True

        if tree[ord(node)-65][1] != '.' and not visited[ord(tree[ord(node)-65][1])-65]:
            inorder_traverse(tree[ord(node)-65][1], visited)


def postorder_traverse(node, visited, answer):
    answer.append(node)
    visited[ord(node)-65] = True
    if tree[ord(node)-65][1] != '.' and not visited[ord(tree[ord(node)-65][1])-65]:
        visited[ord(tree[ord(node)-65][1])-65] = True
        postorder_traverse(tree[ord(node)-65][1], visited, answer)

        if tree[ord(node)-65][0] != '.' and not visited[ord(tree[ord(node)-65][0])-65]:
            visited[ord(tree[ord(node)-65][0])-65] = True
            postorder_traverse(tree[ord(node)-65][0], visited, answer)

    elif tree[ord(node)-65][1] == '.':
        visited[ord(node)-65] = True
        if tree[ord(node)-65][0] != '.' and not visited[ord(tree[ord(node)-65][0])-65]:
            postorder_traverse(tree[ord(node)-65][0], visited, answer)

    return answer

visited = [False]*N
preorder_traverse("A", visited)
print()
visited = [False]*N
inorder_traverse("A", visited)
visited = [False]*N
answer = []
print()
Nanswer = (postorder_traverse("A", visited, answer))
for i in range(len(Nanswer)-1,-1,-1):
    print(Nanswer[i], end='')

