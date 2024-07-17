### Input: x = 121
##Output: true
## Explanation: 121 reads as 121 from left to right and from right to left.

def isPalindrome(x: int) -> bool:
    midPoint = 0
    front_idx = 0
    strX = str(x)
    rear_idx = len(strX)-1

    if ((len(strX) % 2) != 0):
        midPoint = int(len(strX)) + 1

    while (front_idx <= int(len(strX)) + 1 and rear_idx >= midPoint):
        print("front_idx :",front_idx,"  rear_idx:",rear_idx)
        front_slider = strX[front_idx]
        rear_slider = strX[rear_idx]
        if (front_slider != rear_slider):
            return False
        elif (midPoint != 0 and midPoint == front_idx):
            return True
        front_idx = front_idx+1
        rear_idx = rear_idx-1
    return True

print(isPalindrome(-10))


