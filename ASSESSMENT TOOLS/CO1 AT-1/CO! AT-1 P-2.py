blocked = {(2,2), (2,3), (3,3), (4,2), (4,4)}
start = (1,1)
goal = (5,5)
moves = [("Up",(-1,0)), ("Down",(1,0)),
         ("Left",(0,-1)), ("Right",(0,1))]

def neighbors(s):
    for name, (dr, dc) in moves:
        n = (s[0]+dr, s[1]+dc)
        if 1 <= n[0] <= 5 and 1 <= n[1] <= 5 and n not in blocked:
            yield n

stack = [start]
parent = {start: None}

while stack:
    current = stack.pop()
    if current == goal:
        break

    successors = list(neighbors(current))
    for nxt in reversed(successors):
        if nxt not in parent:
            parent[nxt] = current
            stack.append(nxt)

path = []
node = goal
while node is not None:
    path.append(node)
    node = parent[node]

path.reverse()
print("Path:", path)
print("Cost:", len(path)-1)
