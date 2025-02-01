import sys
arr = list(map(int, input().split()))
text = 'ABCDE'

def catchtext(arr):
    for el in arr:
        ans.append(el)

ans = []
tmpans = []
ans.append([text,sys.maxsize])
# 4
for i in range(5):
    point = 0
    for j in range(5):
        if j != i:
            point += arr[j]
    tmpans.append([text[:i]+text[i+1:], point])

catchtext(sorted(tmpans, key=lambda x: (-x[1], x[0])))

# 3
tmpans = []
for i in range(5):
    for j in range(i+1,5):
        point = 0
        for k in range(5):
            if i != k and j != k:
                point += arr[k]
        tmpans.append([text[:i]+text[i+1:j]+text[j+1:], point])
catchtext(sorted(tmpans, key=lambda x: (-x[1], x[0])))

# 2
tmpans = []
for i in range(5):
    for j in range(i+1,5):
        point = 0
        for k in range(5):
            if i == k or j == k:
                point += arr[k]
        tmpans.append([text[i]+text[j], point])
catchtext(sorted(tmpans, key=lambda x: (-x[1], x[0])))

# 1
tmpans = []
for i in range(5):
    tmpans.append([text[i], arr[i]])
catchtext(sorted(tmpans, key=lambda x: (-x[1], x[0])))

ans = sorted(ans, key=lambda x: (-x[1], x[0]))
for el in ans:
    print(el[0])