result = 0
side = 1001
spiral = side*side

for i in reversed(range(1,side + 1, 2)):
    for p in range(0,4):
        if spiral <= 1:
            break
        result += spiral
        spiral -= (i-1)
result += 1
print(result)