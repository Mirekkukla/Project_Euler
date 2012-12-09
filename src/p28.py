total = 0
side = 1001
spiral = side*side

for i in reversed(range(1,side + 1, 2)):
    for j in range(0,4):
        if spiral <= 1:
            break
        total += spiral
        spiral -= (i-1)
total += 1
print(total)