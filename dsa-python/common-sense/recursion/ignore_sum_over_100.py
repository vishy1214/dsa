
hash= {}
sum=0
def add_until_100(array,sum):
    if(len(array)==0):
        return 0

    temp = sum + add_until_100( array[:len(array)-1],sum)

    if(temp <= 100):
        sum = temp
    else:
        print(f'ignoring')
    return sum

print(add_until_100([2,4,33,44,22,15,16],sum))
