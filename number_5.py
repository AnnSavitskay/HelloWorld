def way(mat, ver, met, v1):
    for i in range(0, len(ver)):
        if mat[v1-1][i] != 0 and ver[v1-1] + mat[v1-1][i] < ver[i]:
            ver[i] = ver[v1-1] + mat[v1-1][i]
    met[v1-1] = -1
#    print(ver)
#    print(met)
    if met.count(-1) == len(met):
 #       print(ver)
 #       print(met)
        return ver
    else:
        for i in range(0, len(ver)):
            if mat[v1-1][i] != 0 and met[i] != -1:
                return way(mat, ver, met, i+1)

def way_back(mat, ans, v2, v1, ans_put):
    if v2 == v1:
        return ans_put
    else:
        for i in range(0, len(ans)):
        #    print(ans[v2-1])
        #    print(mat[v2-1][i])
        #    print(ans[i])
            if mat[v2-1][i] != 0 and ans[v2-1] - mat[v2-1][i] == ans[i]:
                ans_put.append(i+1)
                return way_back(mat, ans, i+1, v1, ans_put)


spisok = input().split()
ver_out = []
ver_in = []
vesa = []
ver = []
met = []
c = 1

for sp in spisok:
    if c%3 == 1:
        ver_out.append(sp)
    if c%3 == 2:
        ver_in.append(sp)
    if c%3 == 0:
        vesa.append(sp)
    c = c+1

v1 = int(ver_out[len(ver_out)-1])
v2 = int(ver_in[len(ver_in)-1])
ver_out.pop(len(ver_out)-1)
ver_in.pop(len(ver_in)-1)

vesa = [int(i) for i in vesa]
ver_out = [int(i) for i in ver_out]
ver_in = [int(i) for i in ver_in]

ver_out1 = ver_out.copy()
ver_out1.extend(ver_in)
ver = list(set(ver_out1))
ver = [float('inf') if i != v1 else 0 for i in ver]

met = [0 for i in ver]
mat = [0]*len(ver)
for i in range(len(ver)):
    mat[i] = [0]*len(ver)

for i in range(0, len(ver)):
    for j in range(0, len(ver)):
        for k in range(0, len(ver_out)):
            if ver_out[k] == i+1 and ver_in[k] == j+1:
                mat[i][j] = vesa[k]
                mat[j][i] = vesa[k]

print(v1, v2)
for i in range(0, len(ver)):
    print(mat[i])

ans = (way(mat, ver, met, v1))
print(ans)

ans_put = [v2]
ans_put_1 = way_back(mat, ans, v2, v1, ans_put)
ans_put_1.reverse()
print(ans_put_1)

#print(ver_out)
#print(ver_in)
#print(v1, v2)
#print(mat)
#print(ver)
