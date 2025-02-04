'''
The Hamming weight of a number is the number of set bits (1-bits) in its binary representation. Given a positive integer n, return an array where the ith element is the Hamming weight of integer i for all integers from 0 to n.

Example:
Input: n = 7
Output: [0, 1, 1, 2, 1, 2, 2, 3]
Explanation:

Number
Binary representation
Number of set bits
0	0	0
1	1	1
2	10	1
3	11	2
4	100	1
5	101	2
6	110	2
7	111	3


'''


from typing import List

def hamming_weights_of_integers(n: int) -> List[int]:
    # Write your code here
    dictA = {}
    for i in range(n+1):
        dictA[i] = bin(i).count('1')

    res = []

    for value in dictA.values():
        res.append(value)
    return res

    
