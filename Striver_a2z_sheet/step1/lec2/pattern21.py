'''
https://www.naukri.com/code360/problems/ninja-and-the-star-pattern-i_6581920?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems&leftPanelTabValue=DISCUSS
Ninja and the Star pattern1
***
* *
***
'''


def getStarPattern(n: int) -> None:
    # Write your solution here.
    for row in range(n):
        for col in range(n):
            if row==0 or row== n -1 or col==0 or col== n -1:
                print("*" ,end="")
            else:
                print(" ", end="")
        print()

    pass


num = int(input())
getStarPattern(num)