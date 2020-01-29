from typing import TypeVar

Element = TypeVar("Element")

def printArray(array: [Element]):
    for element in array:
        print(element)

m = int(input())
vInt = []
for i in range(m):
	vInt.append(int(input()))

n = int(input())
vString = []
for i in range(n):
	vString.append(input())

printArray(vInt)
printArray(vString)