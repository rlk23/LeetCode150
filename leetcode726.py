'''
Given a string formula representing a chemical formula, return the count of each atom.

The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.

One or more digits representing that element's count may follow if the count is greater than 1. If the count is 1, no digits will follow.

For example, "H2O" and "H2O2" are possible, but "H1O2" is impossible.
Two formulas are concatenated together to produce another formula.

For example, "H2O2He3Mg4" is also a formula.
A formula placed in parentheses, and a count (optionally added) is also a formula.

For example, "(H2O2)" and "(H2O2)3" are formulas.
Return the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.

The test cases are generated so that all the values in the output fit in a 32-bit integer.

 

Example 1:

Input: formula = "H2O"
Output: "H2O"
Explanation: The count of elements are {'H': 2, 'O': 1}.
Example 2:

Input: formula = "Mg(OH)2"
Output: "H2MgO2"
Explanation: The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
Example 3:

Input: formula = "K4(ON(SO3)2)2"
Output: "K4N2O14S4"
Explanation: The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
 

Constraints:

1 <= formula.length <= 1000
formula consists of English letters, digits, '(', and ')'.
formula is always valid.

'''

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n = len(formula)
        i = 0 
        charMap = {}
        stack = []

        while i < n:
            c = formula[i]

            if c == "(":
                stack.append(charMap)
                charMap = {}
                i+= 1
            elif c == ")":
                i += 1

                multiplier = 0

                while i < n and formula[i].isdigit():
                    multiplier = multiplier * 10 + int(formula[i])
                    i += 1

                if multiplier == 0:
                    multiplier = 1
                
                for atom in charMap:
                    charMap[atom] *= multiplier
                
                oldMap = stack.pop()

                
                for atom, count in charMap.items():
                    oldMap[atom] = oldMap.get(atom, 0) + count

                # Now go back to using oldMap as the current map
                charMap = oldMap


            else:
                elem_start = i  # remember where the element begins
                i += 1  # we've read the uppercase letter
                while i < n and formula[i].islower():
                    i += 1
                elementName = formula[elem_start:i]

                # Parse count
                count = 0
                while i < n and formula[i].isdigit():
                    count = count * 10 + int(formula[i])
                    i += 1
                if count == 0:
                    count = 1

                # Add to current charMap
                charMap[elementName] = charMap.get(elementName, 0) + count

        result = []
        for element in sorted(charMap.keys()):
            result.append(element)
            if charMap[element] > 1:
                result.append(str(charMap[element]))
        return "".join(result)
