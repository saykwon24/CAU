import numpy as np
import re

# ==========================================
# 1. Required Classes
# ==========================================
class Stack:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return len(self.items) == 0
        
    def push(self, e):
        self.items.append(e)
        
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
        
    def peek(self): 
        if not self.is_empty():
            return self.items[-1]
        return None
        
    def __str__(self):
        return str(self.items)

class Queue:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return len(self.items) == 0
        
    def enqueue(self, e):
        self.items.append(e)
        
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None
        
    def __str__(self):
        return str(self.items)

# ==========================================
# 2. Stack
# ==========================================
def tokenize(expr):
    """Helper function to split the expression into numbers, variables, and operators"""
    return re.findall(r'\d+|[A-Z]+|[-+*/()]', expr)

## 1. Convert infix expression to postfix
def infix_to_postfix(expr, label=""):
    """Implementation based on Algorithm 13 convert() from lecture notes"""
    tokens = tokenize(expr)
    S = Stack()
    postfix = []
    
    # Define operator precedence ('(' acts as the lowest precedence inside the stack)
    P = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}
    
    # 2-space indentation for sub-problem label
    print(f"  ({label}) Converting: {expr}")
    
    for s in tokens:
        # if isOperand(s) then write(s)
        if re.match(r'\d+|[A-Z]+', s):
            postfix.append(s) 
        # else if s = '(' then S.push(s)
        elif s == '(':
            S.push(s) 
        # else if s = ')' then 
        elif s == ')':
            while not S.is_empty() and S.peek() != '(':
                postfix.append(S.pop())
            S.pop() # remove '('
        # else (s is an operator)
        else:
            while not S.is_empty() and P[s] <= P[S.peek()]:
                postfix.append(S.pop()) 
            S.push(s)
        
        # 4-space indentation and <45 alignment for safe column width
        print(f"    Token: {s:<3} | Stack S: {str(S):<45} | Postfix: {' '.join(postfix)}")
        
    # while !S.isEmpty() do write(S.pop())
    while not S.is_empty():
        postfix.append(S.pop()) 
        print(f"    Token: {'END':<3} | Stack S: {str(S):<45} | Postfix: {' '.join(postfix)}")
        
    result = ' '.join(postfix)
    print(f"    >> Resulting Postfix: {result}\n")

## 2. Push operation on a bounded array stack
def push_bounded(S_arr, e):
    """Overwrites the oldest element if the stack is full, maintaining LIFO logic for pop"""
    if 'NA' in S_arr:
        # If there is an empty space (NA), insert at the first NA position
        idx = np.where(S_arr == 'NA')[0][0]
        S_arr[idx] = e
    else:
        # If full, remove the oldest element (index 0) and shift left
        S_arr[:-1] = S_arr[1:]
        S_arr[-1] = e

# ==========================================
# 3. Queue
# ==========================================

## 1. Reverse the order of queue elements
def reverseQueue(Q, label=""):
    """Reverses elements in Q using only an empty Stack and enqueue/dequeue"""
    S = Stack()
    
    # 2-space indentation
    print(f"  ({label}) Reversing Queue: {str(Q)}")
    
    # Queue -> Stack (dq: dequeue, pu: push)
    while not Q.is_empty():
        S.push(Q.dequeue())
        print(f"    Action: {'dq->pu':<6} | Stack S: {str(S):<40} | Queue Q: {str(Q)}")
        
    # Stack -> Queue (po: pop, en: enqueue)
    while not S.is_empty():
        Q.enqueue(S.pop())
        print(f"    Action: {'po->en':<6} | Stack S: {str(S):<40} | Queue Q: {str(Q)}")
        
    print(f"    >> Reversed Queue: {str(Q)}\n")

## 2. Deque implementation using two stacks
class Deque:
    def __init__(self):
        self.S1 = Stack()
        self.S2 = Stack()
        
    def print_states(self, action):
        # 4-space indentation for tracking output
        print(f"    Action: {action:<10} | S1: {str(self.S1):<15} | S2: {str(self.S2)}")
        
    def push(self, e):
        self.S1.push(e)
        self.print_states(f"push({e})")
        
    def inject(self, e):
        self.S2.push(e)
        self.print_states(f"inject({e})")
        
    def pop(self):
        if self.S1.is_empty():
            while not self.S2.is_empty():
                self.S1.push(self.S2.pop())
        val = self.S1.pop()
        self.print_states("pop()")
        return val
        
    def eject(self):
        if self.S2.is_empty():
            while not self.S1.is_empty():
                self.S2.push(self.S1.pop())
        val = self.S2.pop()
        self.print_states("eject()")
        return val

# ==========================================
# 4. Tree
# ==========================================
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

# Template class exactly as designated in Algorithm 4
class Tree:
    def __init__(self):
        self.root = None
        
    def isroot(self, v):
        return v == self.root
        
    def child(self, v):
        return v.children

## 1. Count internal and external nodes
def countInternalNodes(T, node=None, is_start=True):
    if is_start: node = T.root
    if node is None: return 0
    # Must use the designated T.child() method
    children = T.child(node)
    if not children: return 0
    count = 1
    for c in children: count += countInternalNodes(T, c, False)
    return count

def countExternalNodes(T, node=None, is_start=True):
    if is_start: node = T.root
    if node is None: return 0
    children = T.child(node)
    if not children: return 1
    count = 0
    for c in children: count += countExternalNodes(T, c, False)
    return count

## 2. Calculate various path lengths
def PathLength(T, node=None, depth=0, is_start=True):
    if is_start: node = T.root
    if node is None: return 0
    total = depth
    for c in T.child(node): total += PathLength(T, c, depth + 1, False)
    return total

def intPathLength(T, node=None, depth=0, is_start=True):
    if is_start: node = T.root
    if node is None: return 0
    children = T.child(node)
    if not children: return 0
    total = depth
    for c in children: total += intPathLength(T, c, depth + 1, False)
    return total

def extPathLength(T, node=None, depth=0, is_start=True):
    if is_start: node = T.root
    if node is None: return 0
    children = T.child(node)
    if not children: return depth
    total = 0
    for c in children: total += extPathLength(T, c, depth + 1, False)
    return total

# ==========================================
# 5. Execution & Output
# ==========================================
if __name__ == "__main__":
    
    # ------------------------------------
    # Stack Output
    # ------------------------------------
    print("-" * 60)
    print(" [Stack] Q1. Converting Infix to Postfix")
    print("-" * 60)
    expr_a = "4*3-(17+3)/(5*(6-15/3+1))"
    expr_b = "(A-(B-C))*D-(E*(F-G+H))/I"
    infix_to_postfix(expr_a, "a")
    infix_to_postfix(expr_b, "b")
    
    print("-" * 60)
    print(" [Stack] Q2. Bounded Stack")
    print("-" * 60)
    # dtype=object to support both string 'NA' and integers safely
    S_arr = np.array(['NA', 'NA', 'NA'], dtype=object)
    for i in range(6):
        push_bounded(S_arr, i)
        print(f"    Action: push({i}) -> Array S: {S_arr}")
    print(f"    >> Final Array S: {S_arr}\n")

    # ------------------------------------
    # Queue Output
    # ------------------------------------
    print("-" * 60)
    print(" [Queue] Q1. reverseQueue")
    print("-" * 60)
    Q_a = Queue()
    for char in ['r', 'a', 'c', 'e', 'c', 'a', 'r']: Q_a.enqueue(char)
    reverseQueue(Q_a, "a")
    
    Q_b = Queue()
    for char in ['q', 'u', 'e', 'u', 'e']: Q_b.enqueue(char)
    reverseQueue(Q_b, "b")
    
    print("-" * 60)
    print(" [Queue] Q2. Deque using Stacks")
    print("-" * 60)
    D = Deque()
    D.push(1)
    D.inject(2)
    D.pop()
    D.pop()
    D.inject(3)
    D.push(4)
    D.eject()
    D.eject()
    print()

    # ------------------------------------
    # Tree Output
    # ------------------------------------
    print("-" * 60)
    print(" [Tree] Nodes & Path Lengths")
    print("-" * 60)
    
    # Construct an arbitrary tree for testing
    T = Tree()
    T.root = TreeNode("Root")
    nodeA = TreeNode("A"); nodeB = TreeNode("B")
    nodeC = TreeNode("C"); nodeD = TreeNode("D")
    nodeE = TreeNode("E")
    
    T.root.children = [nodeA, nodeB]
    nodeA.children = [nodeC, nodeD]
    nodeB.children = [nodeE]
    
    # Visual description of the test tree structure
    print("  [Test Tree Structure]")
    print("    Root")
    print("    ├── A")
    print("    │   ├── C")
    print("    │   └── D")
    print("    └── B")
    print("        └── E\n")
    
    # Q1: Node Counting
    print("  Q1. Node Counting")
    print(f"    (a) {'Internal Nodes Count':<23} : {countInternalNodes(T)}")
    print(f"    (b) {'External Nodes Count':<23} : {countExternalNodes(T)}\n")
    
    # Q2: Path Lengths
    print("  Q2. Path Lengths")
    print(f"    >> {'Path Length':<24} : {PathLength(T)}")
    print(f"    >> {'Internal Path Length':<24} : {intPathLength(T)}")
    print(f"    >> {'External Path Length':<24} : {extPathLength(T)}\n")