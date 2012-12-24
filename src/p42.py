import csv
import math
import string
from functions.words import *

d = alphabetDict()

def isTriangle(n):
    candidate = math.floor(math.sqrt(2*n))
    if int(.5*candidate*(candidate + 1)) == int(n):
        return True
    else:
        return False

totalTriangles = 0
cr = csv.reader(open("files/p42data","r"))
for row in cr:
    for word in row:
        score = 0
        for i in str(word).lower():
            score += d[i]
        if isTriangle(score):
            totalTriangles += 1

print(totalTriangles)