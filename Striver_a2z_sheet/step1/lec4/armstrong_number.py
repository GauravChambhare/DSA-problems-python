"""
https://www.naukri.com/code360/problems/armstrong-number_1462443?leftPanelTabValue=PROBLEM
"""

def isArmstrong(num):
    # Write your code here.
    power = len(str(num))
    sum = 0
    for x in str(num):
        sum = sum + int(x)**power
    if sum==num:
        return "YES"
    else:
        return "NO"
    pass


i = int(input())
print(isArmstrong(i))
