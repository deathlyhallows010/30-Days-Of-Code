# Enter your code here. Read input from STDIN. Print output to STDOUT
def func(arr):
    string = ''
    for i in range(0,len(arr),2):
        string+=arr[i]
    string+=' '
    for i in range(1,len(arr),2):
        string+=arr[i]
    return string

T = int(input())

S = []
for i in range(T):
     S.append(input())

for i in range(T):
    print(func(S[i]))


