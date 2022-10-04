# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30

@author: Parth Shah

Problem Statement:
    
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
       
"""
from typing import Optional, Union

# Definition for Singly Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# Defination of Linked List
class LinkedList:
   def __init__(self):
      self.headval = None
        
# Function Allows User to Create List Node Object With Specified Array 
def defineListNode(arr: list): 
    if len(arr) != 0:
        return(LinkedList())
    
    Nodes = []
    for index, value in enumerate(arr):
        Nodes.append(ListNode(value))
        
    for index, node in enumerate(Nodes):
        if index < (len(Nodes) - 1):
            Nodes[index].next = Nodes[(index + 1)]
        
    l = LinkedList()
    l.headval = Nodes[0]
    return(l)
        
# Function Calculations the Sum of Two Linked Links With Values Stored in Reverse Order
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]):
    
    result = []
    
    while l















