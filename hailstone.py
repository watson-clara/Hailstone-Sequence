#!/usr/bin/python

# Author: Clara Watson
# Date: July 11, 2020
# Description:  takes a positive integer parameter as the initial number of a hailstone sequence and returns how many steps it takes to reach 1

def hailstone(posInput):
    if posInput <= 1:
    	return posInput
    isOne = False
    count = 0 
    while (isOne == False):
        count = count + 1
        if (posInput % 2) == 0:
            posInput = posInput/2
        else:
            posInput = posInput * 3
            posInput = posInput + 1
        if (posInput == 1):
            isOne = True
            break
        else:
            isOne = False
    return count
