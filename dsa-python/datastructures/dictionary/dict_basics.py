import math

pairs = {"1":0,"2":2}
pairs2 = {}


print(len(pairs))
print(pairs.get(1))  # None
print(pairs.get("1")) # 0
print(pairs.get(4)) # None

arr = [1,2,4,5,2,1]

print("~~~~~~~~~~~~~~"*3)
for x in arr:
    if(pairs2.get(x) == None):
        pairs2[x] = 1
    else:
        pairs2[x] = pairs2.get(x) + 1

print(pairs2)


for index,key in enumerate(pairs2):
    print(f'{index} : {key}')


def sockMerchant(ar):
    # Write your code here
    pairs = {}
    pairCounter = 0
    for x in ar:
        if(pairs.get(x) == None):
            pairs[x] = 1
        else:
            pairs[x] = pairs.get(x)+1

    for p in pairs:
        val = pairs.get(p)
        print(pairCounter)
        if(val>1 and val % 2 == 0):
            pairCounter = pairCounter + math.floor(val / 2)
        elif(val>1 and val % 2 != 0):
            pairCounter = pairCounter + math.floor((val - 1) / 2)

    return pairCounter

print(sockMerchant(arr))