# Enter your code here. Read input from STDIN. Print output to STDOUT

checkOut = str(input()).split(" ")
da = int(checkOut[0])
ma = int(checkOut[1])
ya = int(checkOut[2])

checkIN = str(input()).split(" ")
de = int(checkIN[0])
me = int(checkIN[1])
ye = int(checkIN[2])

fine = 0

if ya > ye:
    fine = 10000
elif ya == ye:
    if ma > me:
        fine = (ma - me) * 500
    elif ma == me and da > de:
        fine = (da - de) * 15

print(fine)