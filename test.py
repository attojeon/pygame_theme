from sys import stdin

sum = 0
n = int( stdin.readline() )
for x in range(1, n ):
    if( x % 3 == 0):
        sum += x
        #print("{}:{}".format(x, sum))
print(sum)