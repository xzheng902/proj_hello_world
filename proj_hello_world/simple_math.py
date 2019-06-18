# simple_math.py
# Mike Zheng
# 6/18/19
# simple python script

def mean(list):
    """Function that returns the mean of a list"""
    sum = 0
    for num in list:
        sum += num
    return sum/len(list)
