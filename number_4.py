n = int(input())
treug = [1]

print(*treug)

for i in range(1, n):
    treug = [treug[i-1] + treug[i] if i > 0 and i < len(treug)
             else treug[0]+0 for i in range(0, len(treug))]
    treug.append(1)
    print(*treug)
