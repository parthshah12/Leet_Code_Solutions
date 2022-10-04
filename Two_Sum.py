# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30

@author: Parth Shah

Problem Statement:
    
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Possible Edge Cases: 

    1) Empty Array
    2) Repeating Numbers
    3) Array With Numbers Not Summing to Target
    4) Float Values
    
Logic: 
    
    Brute Force Method: Iterate Through All Two Pair Combinations Until A Sum of Two Number is Found That Equals to the Target Value
    Time Complexity: O(n^2)
    
    Hashmap Method: Use A Dictionary With Key, Value Pairs Equalto the Array Element Value and the Index. 
                    For Each Iteration Check if the Required Difference is A Key in The Dictionary. 
                    
    Time Complexity: O(n)     
     
"""

import time

# Optimal Method
def Two_Sum_Optimal(arr: list[float], target_value: float) -> list[list[float]]:
    prior_values = {}
    for index, value in enumerate(arr):
        diff = target_value - value
        if diff in prior_values:
            return([value, diff])
        prior_values[value] = index
    return([])
        
# Brute Force Method
def Two_Sum_Brute_Force(arr: list[float], target_value: float) -> list[float]:    
    if len(arr) == 0:
        return([])
    
    for i in range(len(arr)):
        value_1 = arr[i]
        diff = round(target_value - value_1,10)
        
        for j in range(i,len(arr)):
            if arr[j] == diff:
                print([arr[i], arr[j]])
                return ([arr[i], arr[j]])         
    return([])

# Unit Test
def Unit_Test(function: object):
    
    # Case 1: Empty Array
    assert function([], 10) == [] 
    
    # Case 2: Repeating Value
    assert function([6,6,4,4,3,2], 10) == [6,4] or function([6,6,4,4,3,2], 10) == [4,6]
    
    # Case 3: Array With Numbers Not Summing to Target
    assert function([1,2,3], 10) == [] 
    
    # Case 4: Floating Point Numbers
    assert function([1.2,9.6,0.4,2.3],10) == [9.6,0.4] or function([1.2,9.6,0.4,2.3],10) == [0.4, 9.6]

    print("Unit Test Passed")
    
if __name__ == "__main__":
    
    Unit_Test(Two_Sum_Brute_Force)
    Unit_Test(Two_Sum_Optimal)
    
    start = time.time()
    Two_Sum_Optimal([1,6,11,7,10,-1] + [1]*100, 10)
    end = time.time()
    print(end - start)
    
    start = time.time()
    Two_Sum_Brute_Force([1,6,11,7,10,-1] + [1]*100, 10)
    end = time.time()
    print(end - start)

    
    
    
    
    
    
    

        
        
        
    
    
    
    
















